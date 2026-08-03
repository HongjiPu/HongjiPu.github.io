---
layout: page
title: "Experience"
subtitle: "Research, quantitative strategy, and investment work across academia, sell-side, buy-side, and venture."
eyebrow: "Track record"
permalink: /experiences/
---

## Research
<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Neural Network Optimization for Option Pricing</span><span class="entry__date">2025.09</span></span>
    <span class="entry__row"><span class="entry__role">Independent Researcher</span><span class="entry__org">Matthew Murphy(UIUC)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Problem Formulation:</strong> Investigated the acceleration of Early Exercise Premium (EEP) calculations using deep learning. Modeled the implied volatility surface via <strong>SSVI</strong> and optimized the fitting process using the <strong>SLSQP algorithm</strong>.</p>
    <p><strong>Methodology:</strong> Designed a Feedforward Neural Network (FNN) to learn the non-linear mapping from SSVI surface parameters to EEP. Implemented a <strong>dual-phase framework</strong> (Offline/Online) to bridge the gap between numerical methods and real-time inference.</p>
    <p><strong>Performance:</strong> Achieved a <strong>10x reduction in RMSE</strong> compared to traditional approximations. The Fast-NN variant demonstrated significant generalization across varying market conditions (k, r, q, T).</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Revisiting Man vs. Machine Learning</span><span class="entry__date">2025.03</span></span>
    <span class="entry__row"><span class="entry__role">Research Assistant</span><span class="entry__org">Prof. Yangdi Zhu</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Predictive Modeling:</strong> Evaluated the efficiency of analyst earnings forecasts by implementing a <strong>75-feature Random Forest (RF)</strong> regressor. Extended Binsbergen et al. (2023) by introducing <strong>LASSO and LightGBM</strong> as comparative benchmarks.</p>
    <p><strong>Robustness & Evaluation:</strong> Conducted exhaustive sensitivity analysis across 48 RF variants. Controlled for systematic biases using <strong>Fama-French 5-Factor models</strong> to isolate the machine learning premium from known anomalies.</p>
  </div>
</details>

<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Risk Spillover Effects in Digital Financial Market</span><span class="entry__date">2024.01</span></span>
    <span class="entry__row"><span class="entry__role">Research Assistant</span><span class="entry__org">Prof. Bianling Ou</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Systemic Risk Modeling:</strong> Developed a multi-market risk assessment framework covering stock, bond, and FX markets. Employed <strong>GARCH-family models</strong> and <strong>Monte Carlo simulations</strong> to estimate joint distributions of Value-at-Risk (VaR).</p>
    <p><strong>Causal Inference:</strong> Utilized Structural Vector Autoregression (SVAR) and Error Correction Models (VECM) to quantify the impulse response of fintech expansion on financial stability.</p>
  </div>
</details>

## Intern
<details class="entry">
  <summary>
    <span class="entry__row"><span class="entry__title">Volatility-Targeted Strategies</span><span class="entry__date">2026.01 - 2026.04</span></span>
    <span class="entry__row"><span class="entry__role">Quantitative Research Intern (Practicum)</span><span class="entry__org">JPM Chase（US）</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><em>Details pending...</em></p>
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