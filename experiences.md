---
layout: page
title: "Experience"
subtitle: "Research in language agents, world models, and trustworthy evaluation — alongside quantitative work across the sell-side, buy-side, AI labs, and venture capital."
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
    <span class="entry__row"><span class="entry__title">RubricGuard: Improving LLM Graders Without Breaking Correct Judgments</span><span class="entry__date">2026.03 - Present</span></span>
    <span class="entry__row"><span class="entry__role">Data Science and Engineering Lab (DSE) · Prof. Jiliang Tang</span><span class="entry__org">Michigan State University (US)</span></span>
    <span class="entry__hint">Click to expand / 点击展开详情</span>
  </summary>
  <div class="entry__body">
    <p><strong>Method:</strong> Developed RubricGuard, a Route–Generate–Audit framework for refining LLM grading rubrics without retraining the underlying model. The framework localizes failures to specific score boundaries, generates targeted rubric patches, and audits each update for both target improvement and protected-boundary regressions, limiting scoring-standard drift.</p>
    <p><strong>Results:</strong> Evaluated on ASAP 2.0, EIR, and ASAP-SAS across three LLM backbones, achieving the best performance in <strong>20 of 27</strong> metric–dataset–backbone settings. Boundary-level ablations showed that retaining the audit component reduced protected-case breakage from <strong>15.7% to 3.6%</strong>, confirming its role in preserving previously correct grading decisions.</p>
    <p><strong>Related paper:</strong> RubricWorld — World Model-Guided Rubric Optimization for LLM Graders, under review at AAAI 2026.</p>
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

---

## Technical Toolbox

<div style="text-align: justify;">
  <p><strong>Programming:</strong> Python, SQL, Bash, MATLAB, Lean.</p>
  <p><strong>Tools &amp; Platforms:</strong> PyTorch, Hugging Face Transformers, verl, PyMARL, EPyMARL, MemOS, AgentDojo, NLIP, Qdrant, Git.</p>
</div>
