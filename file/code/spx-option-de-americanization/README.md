# SPX Option De-Americanization — Surfaces, Trees, and the Early Exercise Premium

Research code for extracting the **early exercise premium (EEP)** from American
SPX index options, so an American quote can be converted into the European price
a calibration routine actually wants. The pipeline runs in one direction: fit an
arbitrage-free implied volatility surface, differentiate it into a local
volatility surface, price the same contract by three independent numerical
methods, and measure the gap early exercise opens up.

Data is not included — the study uses SPX option chains from 2011–2023, which
are licensed. Every notebook reads from a `data/` directory you supply.
Outputs were stripped before publishing, so each notebook needs one full
execution before its figures reappear.

---

## The algorithm, step by step

### 1 · Implied volatility surface — SSVI

`01_ssvi_surface_fit.ipynb` · `02_ssvi_calibration.ipynb`

The raw surface is fitted with the **power-law surface SSVI** parameterisation.
In log-moneyness `k` and maturity `T`, total implied variance is

```
w(k, T) = ½ · θ(T) · ( 1 + ρ·φ(θ)·k + sqrt( (φ(θ)·k + ρ)² + 1 − ρ² ) )
φ(θ)    = η · θ(T)^(−γ)
```

Rather than fitting the at-the-money term structure `θ(T)` freely, it is given a
**two-factor mean-reverting form** in `compute_theta_t`:

```
θ(T) = θ∞·T + (V − θ∞)·(1 − e^(−κ₁T))/κ₁
            + (V′ − θ∞)·(κ₁/(κ₁ − κ₂))·[ (1 − e^(−κ₂T))/κ₂ − (1 − e^(−κ₁T))/κ₁ ]
```

so the entire surface across all maturities is carried by six parameters
`(ρ, η, γ, V, V′, θ∞)` with the reversion speeds `κ₁ = 5.5`, `κ₂ = 0.1` fixed.

`02` does the cleaning that has to come first — dropping missing and zero-DTE
quotes, computing the forward `F(t,T)` and log-moneyness, and scoring fit quality
as the share of quotes reproduced inside a tolerance band. The objective is plain
squared error on implied volatility,
`Σ (σ_SSVI(k,T) − σ_obs)²`, minimised with SciPy under box bounds
(`ρ ∈ [−1,1]`, `γ ∈ [0,1]`, `η, V, V′ ≥ 0`) via `TNC`/`SLSQP`.

> **Note on what is runnable here:** the optimizer call in `02` is left
> commented out, and the downstream notebooks consume pre-fitted parameter
> vectors that are pasted in as literals. The fitting objective, bounds, and
> diagnostics are all present; re-running the fit means uncommenting that cell.
> No-arbitrage conditions are enforced only through the box bounds — there is no
> explicit Gatheral–Jacquier constraint in this code, which is why step 2 checks
> the local-variance denominator by hand.

### 2 · Local volatility surface — Dupire

`03_local_volatility.ipynb`

The fitted surface is differentiated **analytically** into local volatility
using Dupire's equation in Gatheral's total-variance form, which needs only
derivatives of `w(k, T)`:

```
σ_loc²(k, T) =            ∂w/∂T
               ─────────────────────────────────────────────────────────
               ( (k/2w)·∂w/∂k − 1 )² + ½·∂²w/∂k² − ¼·(¼ + 1/w)·(∂w/∂k)²
```

`w`, `d_w_d_T`, `d_w_d_k`, and `d2w_dk2` are each written out in closed form, so
these derivatives are exact rather than finite-differenced off a noisy market
surface — which is the whole reason for fitting a parametric surface before
taking this step. The notebook reconstructs the surface under several parameter
sets, including published reference values, to check the denominator stays
positive: a negative local variance means the surface has admitted arbitrage.

### 3 · Lattice pricing and de-Americanization

`04_binomial_pricing.ipynb` · `05_binomial_de_americanization.ipynb`

A **Cox–Ross–Rubinstein tree** with

```
u = exp(σ√Δt),  d = 1/u,  p = (exp(rΔt) − d)/(u − d)
```

and backward induction taking `max(continuation, intrinsic)` at every node for
the American contract, continuation only for the European one. The difference
between the two, priced on the *same* tree at the *same* volatility, is the early
exercise premium — isolating it this way means tree discretisation error largely
cancels.

`05` runs this at scale: it joins the per-day SSVI parameters onto the option
chain, evaluates `w(k, T)` to get each contract's model implied volatility, then
prices with a vectorised tree. De-Americanization is the inverse problem —
invert the American pricer for the volatility reproducing the market quote,
remove the EEP, and reprice as European.

### 4 · Finite-difference cross-check

`fdm_pricing.py` · `06_fdm_tree_validation.ipynb`

`fdm_pricing.py` prices against a **QuantLib finite-difference grid**
(`FdBlackScholesVanillaEngine` over a `BlackScholesMertonProcess`), with the
market surface loaded as a `BlackVarianceSurface` across a strike × maturity
volatility matrix, a flat rate, and a **flat continuous dividend yield**.

`06` prices the same contracts on an independent tree that instead handles
**discrete dividends by the escrowed-dividend method** — the lattice is built on
`S₀ − Σ PV(Dᵢ)` with a drifted step `u = exp(rΔt + σ√Δt)`, `d = exp(rΔt − σ√Δt)` —
then plots the residual against the grid across strike, maturity, dividend
amount, and time-to-first-dividend. Two methods agreeing to within a tolerance
is the only evidence either is right; and because one treats dividends discretely
and the other as a yield, part of what the residual measures is exactly that
modelling choice.

### 5 · Measuring the premium

`07_early_exercise_premium.ipynb`

Puts it together. The tree here carries a **continuous dividend yield in the
drift**, `u = exp((r−q)Δt + σ√Δt)` with `p = (exp((r−q)Δt) − d)/(u − d)`, and
prices the American and European contracts side by side. For each contract the
implied volatility backed out of each price is compared against the SSVI model
volatility, repeated across step counts (1,000 vs coarser trees) to separate
genuine premium from numerical error. The resulting `diff_put` / `diff_call`
curves against strike are the measurement the study rests on: the EEP is
strongly moneyness-dependent, and for puts in a high-rate regime it is large
enough that ignoring it biases any surface calibrated from American quotes.

### 6 · Dataset for a learned surrogate

`08_de_americanization_dataset.ipynb`

Assembles the supervised feature table for replacing step 3 with a learned
surrogate: SSVI model volatility, tree-implied American and European
volatilities, contract features, and put/call labels, with missing-quote
handling. **The network definition and training loop are not in this
repository** — this notebook ends at the feature table.

---

## Layout

| File | What it does |
| --- | --- |
| `01_ssvi_surface_fit.ipynb` | SSVI and `θ(T)` evaluation, 3-D surface inspection |
| `02_ssvi_calibration.ipynb` | Chain cleaning, forward/log-moneyness, fit objective and bounds, fit diagnostics |
| `03_local_volatility.ipynb` | Analytic Dupire local volatility from the fitted surface |
| `04_binomial_pricing.ipynb` | CRR tree, American and European, single-contract pricer |
| `05_binomial_de_americanization.ipynb` | Daily SSVI join, vectorised tree, implied-volatility inversion |
| `fdm_pricing.py` | QuantLib finite-difference pricer, continuous dividend yield |
| `06_fdm_tree_validation.ipynb` | Escrowed-dividend tree vs finite-difference residuals |
| `07_early_exercise_premium.ipynb` | EEP measurement and its strike dependence |
| `08_de_americanization_dataset.ipynb` | Feature table for the learned surrogate |

## Running it

```
pip install numpy pandas scipy matplotlib plotly QuantLib-Python python-docx
```

Expected inputs: the cleaned option chain at `data/clean_data2023.csv`, per-day
calibrated parameters at `data/ssvi_para.csv`, and for `06` the finite-difference
price tables (`fdm_price_*.csv`). Then run the notebooks in order.
