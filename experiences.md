---
layout: page
title: "Experience"
subtitle: "Research in language agents, world models, and trustworthy evaluation — alongside the quantitative finance work it grew out of, across the sell-side, buy-side, AI labs, and venture capital."
eyebrow: "Selected work"
permalink: /experiences/
---

## Research Experience

<details class="entry" open>
  <summary>
    <span class="entry__row"><span class="entry__title">CounterMem: World-Model-Verified Counterfactual Memory for Language Agents</span><span class="entry__date">2026.04 - Present</span></span>
    <span class="entry__row"><span class="entry__role">Web Intelligent Systems and Engineering Lab · Prof. Yongfeng Zhang</span><span class="entry__org">Rutgers University (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Method:</strong> Developed CounterMem, an RL-based framework for constructing and reusing verified counterfactual memory in language agents. The method generates local alternatives to failed actions, verifies their outcomes with executable world models, stores action contrasts together with evidence and reuse conditions, and trains a DQN selector to decide when retrieved memory should guide a new task.</p>
    <p><strong>Results:</strong> Evaluated on 12 benchmarks across six domains. CounterMem improved ReAct and Reflexion in 24/24 benchmark-agent comparisons with gpt-oss-120b, averaging <strong>+12.6 pp</strong>; across two backbones, four-domain gains reached <strong>8.2–20.4 pp</strong> while task-run token usage fell by <strong>7.7–42.0%</strong>.</p>
    <p><strong>Links:</strong> <a href="https://arxiv.org/abs/2609.31874" target="_blank" rel="noopener">Paper (arXiv:2609.31874)</a> — under review at ICLR 2027.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">RubricWorld: World Model-Guided Rubric Optimization for LLM Graders</span><span class="entry__date">2026.03 - Present</span></span>
    <span class="entry__row"><span class="entry__role">Data Science and Engineering Lab (DSE) · Prof. Jiliang Tang</span><span class="entry__org">Michigan State University (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Problem:</strong> Each edit to an LLM grader's rubric can correct grading errors while degrading decisions that were already correct, and the same edit produces different effects once earlier revisions have changed the rubric state. Prompt and rubric optimizers select edits on aggregate validation performance, so these state-dependent effects are never learned.</p>
    <p><strong>Method:</strong> Developed RubricWorld, a world model-guided framework for state-conditioned rubric optimization. Learning from paired grading decisions taken before and after each edit, it predicts correction and degradation rates at ordinal score boundaries to guide candidate selection; an independent empirical certification step then uses held-out measurements and finite-sample confidence bounds to decide whether an edit is committed.</p>
    <p><strong>Results:</strong> Evaluated on EIR (National), ASAP 2.0, and ASAP-SAS with three frozen LLM graders, achieving the best result in <strong>20 of 27</strong> reported metric comparisons. On ASAP 2.0, RubricWorld raised gpt-5-mini accuracy from <strong>18.20% to 46.70%</strong>. End-to-end ablations showed that removing rubric-state information reduced average accuracy from <strong>40.18% to 35.42%</strong>, while removing the learned edit-effect model reduced it to <strong>27.31%</strong>.</p>
    <p><strong>Links:</strong> <a href="{{ site.url }}/file/papers/RubricWorld.pdf" target="_blank" rel="noopener">Paper (PDF)</a> — submitted to the ARR October 2026 cycle. Supersedes the earlier Route–Generate–Audit prototype (RubricGuard).</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Network World Models as Environments for Algorithm Design on Complex Networks</span><span class="entry__date">2026.03 - Present</span></span>
    <span class="entry__row"><span class="entry__role">Machine Intelligence for Complex Systems Lab · Prof. Liang Zhao</span><span class="entry__org">Emory University (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Method:</strong> Developed an action-conditioned graph world model that explicitly applies intervention semantics before learning the subsequent diffusion dynamics. Integrated the model into an LLM-driven algorithm discovery loop, where it supplies candidate evaluations and counterfactual feedback to guide program generation and refinement.</p>
    <p><strong>Results:</strong> Evaluated transition prediction, multi-step rollouts, and downstream decision quality on held-out graphs and unseen topologies. Achieved <strong>90.2%</strong> candidate preference accuracy on held-out SBM graphs; world-model-only candidate selection attained <strong>1.01% regret</strong> versus 1.13% for simulator-based selection, using no trusted-simulator calls during selection.</p>
    <p><strong>Links:</strong> <a href="https://arxiv.org/abs/2610.01048" target="_blank" rel="noopener">Paper (arXiv:2610.01048)</a> — under review at ICLR 2027.</p>
  </div>
</details>

---

## Industry Experience

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Volatility-Targeted Strategies Design</span><span class="entry__date">2026.01 - 2026.04</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative Research Intern</span><span class="entry__org">JPMorgan Chase &amp; Co. (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Pipeline:</strong> Co-developed an end-to-end volatility-targeting research pipeline for S&amp;P 500 futures, covering data preprocessing, volatility forecasting, exposure allocation, and backtesting.</p>
    <p><strong>Modeling:</strong> Compared statistical and machine-learning estimators — EWMA, GJR-GARCH, HAR-RV, and Random Forest — alongside regime-aware controllers and ensemble strategies.</p>
    <p><strong>Results:</strong> Evaluated estimator–controller combinations on forecasting accuracy, risk-adjusted returns, turnover, and drawdown. In the project backtests, HAR-RV with regime scaling achieved a Sharpe ratio of <strong>0.602</strong> versus 0.575 with naive scaling, reduced maximum drawdown from <strong>18.71% to 17.58%</strong>, and raised the Calmar ratio from 0.355 to 0.364.</p>
    <p><strong>Related paper:</strong> <a href="https://arxiv.org/abs/2608.10375" target="_blank" rel="noopener">Beyond Forecasting: Recasting Volatility Control as a Routing Problem</a> · <a href="https://github.com/HongjiPu/AI4Fin-Routing-Forecasting" target="_blank" rel="noopener">Code</a> — under review at ACM ICAIF 2026.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">S&P 500 Futures and BTC Linked Strategy</span><span class="entry__date">2025.12 - 2026.01</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative Researcher</span><span class="entry__org">Positive Research Ltd. (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Cross-Asset Forecasting:</strong> Validated volatility spillover from S&P 500 to crypto; built hybrid model integrating VIX surface features with BTC L1 data, significantly improving performance during macro events.</p>
    <p><strong>Surface Modeling:</strong> Calibrated Arbitrage-Free Implied Volatility Surfaces via SSVI and Differential Evolution ($WRMSE < 0.006$); extracted ATM Variance and Skew as leading macro indicators.</p>
    <p><strong>Implementation:</strong> Engineered 30+ Alpha signals from 60,000+ hours of BTC tick data; optimized LightGBM via Optuna for 24h volatility forecasting, achieving an out-of-sample IC of 0.46.</p>
    <p><strong>Research:</strong> Written up under <em>Volatility forecasting and control</em> in <a href="{{ site.url }}/research/applications/">Finance AI</a>, alongside the GARCH-family and LSTM baselines it was built on.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Financial LLM & Multimodal Alpha Research</span><span class="entry__date">2025.05 - 2025.07</span></span>
    <span class="entry__row"><span class="entry__role">Intern in AI Lab</span><span class="entry__org">REI-Tech (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>RAG & Fin-Data:</strong> Built a financial RAG prototype with 10k+ instructions from Snowball and East Money; implemented <strong>CoT</strong> prompting to refine logical information extraction from complex earnings reports.</p>
    <p><strong>Multimodal Alpha:</strong> Developed a novel pipeline structuring <strong>YOLO K-line patterns</strong> and <strong>Whisper audio tags</strong> into embeddings, capturing nuanced market sentiment and non-linear signals.</p>
    <p><strong>LLM Tuning:</strong> Fine-tuned <strong>DeepSeek-V1 (LoRA)</strong> for efficient iteration; delivered a sentiment factor achieving <strong>0.038 Peak RankIC</strong>, outperforming Alpha101.</p>
    <p><strong>Research:</strong> Written up under <em>Factor models and LLMs for alpha</em> in <a href="{{ site.url }}/research/applications/">Finance AI</a>. The retrieval failure modes seen here motivated the later work on belief-state RAG.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Deep-Learning Factor Mining Pipeline for A-shares</span><span class="entry__date">2025.01 - 2025.04</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative Researcher</span><span class="entry__org">Hantak Investment Management (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Alpha Generation:</strong> Developed a DL factor mining pipeline for A-shares, enhancing LiqVol anomaly. Integrated <strong>ProbSparse Attention</strong> and <strong>TFT Variable Selection</strong>, elevating monthly <strong>IC from 0.05 to 0.13</strong>.</p>
    <p><strong>Model Optimization:</strong> Implemented rigorous neutralizations (Size, Industry) and AdamW with cyclic learning rates to prevent overfitting.</p>
    <p><strong>Backtesting:</strong> Executed backtests (2010-2023) demonstrating a <strong>15% Sharpe Ratio improvement</strong> and persistent OOS Alpha against CSI 300.</p>
    <p><strong>Research:</strong> Written up under <em>Factor models and LLMs for alpha</em> in <a href="{{ site.url }}/research/applications/">Finance AI</a>.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Fundamental Factor Discovery & Strategy Backtesting</span><span class="entry__date">2023.10 - 2024.07</span></span>
    <span class="entry__row"><span class="entry__role">Intern in Financial Engineering Group</span><span class="entry__org">Guosheng Securities (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Foundational Factor Research:</strong> Mapped supply chain dynamics via web crawling. Utilized <strong>rolling time-series analysis</strong> to investigate lead-lag relationships in pricing efficiency.</p>
    <p><strong>Backtesting Practice:</strong> Executed rigorous strategy protocols; maintained demo accounts and performed <strong>sensitivity analysis</strong> on entry/exit parameters.</p>
    <p><strong>Statistical Modeling:</strong> Employed Stata to estimate factor premiums (OLS/MAD). Leveraged <strong>VAR models</strong> to predict sector-specific premiums.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Green Finance Research</span><span class="entry__date">2022.03 – 2023.03</span></span>
    <span class="entry__row"><span class="entry__role">Research Assistant</span><span class="entry__org">IIGF of CUFE (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Financial Data Engineering:</strong> Automated crawling of green bond data. Optimized database table structures with <strong>Hash Indexes</strong> for high-frequency datasets.</p>
    <p><strong>ESG Visualization:</strong> Developed dynamic modules via <strong>Matplotlib</strong> to track EU carbon futures and forestry carbon sinks.</p>
    <p><strong>Index Tracking:</strong> Assisted in <strong>CSI 300 Green Leading Index</strong> rebalancing; evaluated performance using adjusted Sharpe Ratios and Max Drawdowns.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Industrial Technology Investment Research</span><span class="entry__date">2022.01 – 2022.03</span></span>
    <span class="entry__row"><span class="entry__role">Investment Research Intern (Industrial Tech)</span><span class="entry__org">Source Code Capital (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Sector Analysis:</strong> Researched New Energy/Metaverse sectors; mapped 100+ companies to evaluate <strong>Business Model Scalability</strong> and technical moats.</p>
    <p><strong>Fundamental Modeling:</strong> Performed <strong>Unit Economics</strong> analysis for growth-stage startups; supported multi-million dollar capital allocation via due diligence.</p>
    <p><strong>Insights Extraction:</strong> Captured market insights via expert interviews, translating industry know-how into <strong>structured investment memorandums</strong>.</p>
  </div>
</details>

---

## Earlier Research · Quantitative Finance

<p style="color:var(--muted);font-size:.93rem;max-width:68ch;">
  The work this research grew out of — risk measurement, derivative pricing, and
  factor models — in reverse chronological order. Each item corresponds to a
  project card under <a href="{{ site.url }}/research/applications/">Finance AI</a>.
</p>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Neural-Network Optimization for Pricing and Local-Volatility Surfaces</span><span class="entry__date">2025.09 - Present</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative finance research</span><span class="entry__org">Derivatives pricing</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Scope:</strong> Continuation of the de-Americanization work below, comparing SSVI parameterizations, local-volatility extraction, American binomial trees, and finite-difference solvers against neural surrogates.</p>
    <p><strong>Question:</strong> Which stage of the pricing pipeline the network should actually replace — the surface fit, the early-exercise premium, or the solver itself — rather than treating the pipeline as one black box to approximate.</p>
    <p><strong>Links:</strong> <a href="https://github.com/HongjiPu/HongjiPu.github.io/tree/main/file/code/spx-option-de-americanization" target="_blank" rel="noopener">Code</a> — the shared SSVI / local-volatility / tree / finite-difference codebase, with a README deriving each step.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">BTC Realized Volatility: GARCH-Family and LSTM Baselines</span><span class="entry__date">2025.12</span></span>
    <span class="entry__row"><span class="entry__role">Independent research</span><span class="entry__org">Volatility modelling</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Method:</strong> Forecast seven-day-ahead average realized volatility for BTC-USD from roughly 2,500 daily observations, using the GARCH family — GARCH, TARCH, and variants across interval windows — and then an LSTM over the same engineered features, scored against naive and rolling baselines.</p>
    <p><strong>Framing:</strong> Treated as a trade rather than a regression: forecast realized volatility is compared against market implied volatility, and the sign of the gap decides whether the option is cheap or rich. This set the baseline the cross-asset VIX–BTC model was later measured against.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Man versus Machine Learning Revisited — Replication and Extension</span><span class="entry__date">2025.03 - 2025.07</span></span>
    <span class="entry__row"><span class="entry__role">Research Assistant</span><span class="entry__org">Central University of Finance and Economics (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Replication:</strong> Rebuilt the replication package for Zhang, Zhu and Linnainmaa (<em>Review of Financial Studies</em>, 2025) end to end on WRDS data (CRSP, Compustat, IBES), including the look-ahead-bias-free earnings forecasts and the random-forest replication of Binsbergen et al.</p>
    <p><strong>Benchmarks:</strong> Compared the machine-learning forecasts against the linear forecasts of So (2013) and Hughes et al. (2008), then ran single sorts and Fama–MacBeth regressions over FF49 industries, with alternative random-forest and machine-learning specifications probed for robustness.</p>
    <p><strong>Takeaway:</strong> A carefully implemented linear baseline is the hardest number to beat — a prior I have carried into every evaluation I have designed since.</p>
    <p><strong>Links:</strong> <a href="{{ site.url }}/file/papers/Man-versus-Machine-Learning-Replication-Package.pdf" target="_blank" rel="noopener">Replication notes (PDF)</a> · <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4899584" target="_blank" rel="noopener">Original paper (SSRN)</a></p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">SPX–VIX Joint Calibration with a Neural SDE</span><span class="entry__date">2025.01 - 2025.05</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative finance research</span><span class="entry__org">Volatility surface calibration</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Model:</strong> Built a two-factor stochastic local volatility model in JAX whose drift, diffusion, and correlation parameters are supplied by neural networks and trained through Euler–Maruyama simulation, so SPX and VIX smiles are calibrated jointly and stay arbitrage-free across both markets.</p>
    <p><strong>Variance reduction:</strong> Quasi-Monte Carlo via Sobol sequences improved on antithetic paths, cutting the deviation ratio from <strong>5.02/0.764</strong> (SPX/VIX) to <strong>3.8/0.28</strong> — the deviation ratio measuring model-to-market implied volatility error relative to the bid–ask spread.</p>
    <p><strong>Production scale:</strong> Extended the calibration from 8 maturities to all <strong>38 SPX and 13 VIX</strong> maturities under a warm-start then next-day protocol, training roughly <strong>7× faster</strong> than the reference implementation (0.9 versus 7.86 minutes per 100 epochs).</p>
    <p><strong>Limit found:</strong> Short-dated, deep out-of-the-money SPX calibration remained unstable across quote dates — small Vega makes the implied-volatility gradients overshoot and oscillate — which defines the practical boundary of the model.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Digital Finance and Risk in Traditional Financial Markets</span><span class="entry__date">2024.09 - 2025.01</span></span>
    <span class="entry__row"><span class="entry__role">Undergraduate research</span><span class="entry__org">Central University of Finance and Economics (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Measurement:</strong> Computed VaR-based risk indices for five Chinese financial markets over 2013–2023, then estimated a joint vector autoregression linking those indices to an index of digital-finance development.</p>
    <p><strong>Identification:</strong> Used variance decomposition and impulse response functions to separate how much of each market's risk is attributable to digital finance from how much is common to the system.</p>
    <p><strong>Finding:</strong> Contrary to the premise the paper set out to test, the growth of digital finance is associated with <em>lower</em> risk in the traditional markets it competes with, not higher.</p>
    <p><strong>Links:</strong> <a href="{{ site.url }}/file/papers/Pu-2024-Digital-Finance-Risk-Spillover-VAR.pdf" target="_blank" rel="noopener">Paper (PDF, 中文)</a></p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Long-Horizon Forecasting of the Dow Jones Index with ARMA Models</span><span class="entry__date">2024</span></span>
    <span class="entry__row"><span class="entry__role">Undergraduate research</span><span class="entry__org">Central University of Finance and Economics (CN)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Data:</strong> 1,685 weekly observations of the Dow Jones U.S. index from 1992 to 2024, drawn from Wind.</p>
    <p><strong>Method:</strong> Stationarity testing and differencing, ARMA order selection by information criteria, residual diagnostics, then a ten-year-ahead projection of the series.</p>
    <p><strong>Why it stays on the list:</strong> A deliberately plain baseline, and a useful reference for how little a well-specified linear model concedes to heavier machinery on index-level data.</p>
    <p><strong>Links:</strong> <a href="{{ site.url }}/file/papers/Pu-2024-DJIA-ARMA-Forecast.pdf" target="_blank" rel="noopener">Paper (PDF, 中文)</a></p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Neural-Network De-Americanization for American Option Pricing</span><span class="entry__date">2024.01 - 2024.05</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative finance research</span><span class="entry__org">Derivatives pricing</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Data and surface:</strong> Cleaned SPX index option data from 2011 to 2023 and fitted a power-law surface SSVI model to the raw implied volatility surface.</p>
    <p><strong>Benchmark:</strong> Implemented binomial-tree de-Americanization as the reference method for extracting the early exercise premium, with finite-difference pricing used to generate synthetic option prices for controlled comparison.</p>
    <p><strong>Result:</strong> Stress-tested neural de-Americanization in simulated extreme high- and low-risk-free-rate environments, where it held its pricing accuracy at computational cost comparable to the binomial method — the case for treating the network as a surrogate for a specific numerical step rather than for the whole pipeline.</p>
    <p><strong>Links:</strong> <a href="https://github.com/HongjiPu/HongjiPu.github.io/tree/main/file/code/spx-option-de-americanization" target="_blank" rel="noopener">Code</a> — SSVI surface fit, analytic Dupire local volatility, CRR and escrowed-dividend trees, QuantLib finite differences, and the early-exercise-premium measurement, with a README deriving each step.</p>
  </div>
</details>

---

## Technical Toolbox

<div style="text-align: justify;">
  <p><strong>Programming:</strong> Python, SQL, Bash, MATLAB, Lean.</p>
  <p><strong>Tools &amp; Platforms:</strong> PyTorch, Hugging Face Transformers, verl, PyMARL, EPyMARL, MemOS, AgentDojo, NLIP, Qdrant, Git.</p>
</div>
