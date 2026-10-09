---
layout: page
title: "中文主页"
subtitle: "研究方向、论文、教育背景与近期经历的中文说明。"
eyebrow: "关于我"
permalink: /cn/
lang: zh-CN
---

## 关于我

<img src="{{ site.url }}/{{ site.owner.bio_photo }}" class="floatpic" alt="蒲洪基">

<div style="text-align: justify;">
  <p>首先感谢您的阅读。我是<strong>蒲洪基（Hongji Pu）</strong>，2003 年生，北京人，目前在伊利诺伊大学厄巴纳-香槟分校（UIUC）Grainger 工学院攻读金融工程硕士。</p>

  <p>我的研究方向是<strong>自我进化的语言智能体</strong>、<strong>图世界模型</strong>与<strong>可信 LLM 系统</strong>：研究智能体如何从经验、外部知识和可验证的反馈中改进自己的记忆、可复用技能与决策能力，以及世界模型如何支撑复杂网络上的算法设计。贯穿这些方向的一个共同问题是——系统在修好做错的样本时，能不能不把原本做对的样本弄坏。</p>

  <p>我的出发点是金融系统：如何用数学模型刻画不确定性、度量风险、并在动态环境中支持决策。顺着这个问题往下走，我开始关心更一般的命题——决策系统能否超越预测与优化，去感知、推理、学习并持续适应。这把我带到了今天的 AI 研究。</p>
</div>

---

## 研究方向

| 方向 | 在做什么 |
| --- | --- |
| 可靠性与验证 | 记忆、信念与证据机制，让智能体行为可复现、可审计（CounterMem、BeliefRAG、Launder-Bench） |
| 自我进化智能体 | 从经验与论文中持续吸收新能力，同时不偏离原始目标（Paper2LLM++、SkillOps） |
| 网络世界模型 | 带干预语义的图上动力学建模，作为算法自动设计的评估环境（Network World Models） |
| 高效智能体基础设施 | 画像、路由与编排，让多模型系统在生产中养得起（RouteProfile） |
| 教育 AI | 评分量表的定向修补与回归审计（RubricWorld、RubricGuard） |
| 金融 AI | 把波动率控制重构成路由问题（Beyond Forecasting） |

详细介绍见 [Research]({{ site.url }}/research/)。

---

## 论文（在投 / 预印本）

<p style="color:var(--muted); font-size:.9rem;">† 表示共同第一作者</p>

{% for p in site.data.publications.items %}
- **{{ p.title }}**<br>
  <span style="color:var(--muted);font-size:.92rem;">{{ p.authors | join: ", " }} — {{ p.venue }}</span>{% if p.links %}<br>
  {% for l in p.links %}<a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}{% endif %}
{% endfor %}

完整列表与筛选见 [Publications]({{ site.url }}/publications/)。

---

## 教育背景

* **伊利诺伊大学厄巴纳-香槟分校（UIUC）** — 金融工程硕士（MSFE），2025.08 – 2026.12，GPA 3.54/4.00
* **中央财经大学（CUFE）** — 金融学学士，2021.08 – 2025.06，GPA 3.84/4.00，专业排名 1/39

---

## 科研与实习经历

* **罗格斯大学** Web Intelligent Systems and Engineering Lab，导师 Yongfeng Zhang 教授（2026.04 – 至今）
* **密歇根州立大学** Data Science and Engineering Lab，导师 Jiliang Tang 教授（2026.03 – 至今）
* **埃默里大学** Machine Intelligence for Complex Systems Lab，导师 Liang Zhao 教授（2026.03 – 至今）
* **摩根大通（JPMorgan Chase & Co.）** 量化研究实习生，波动率目标策略设计（2026.01 – 2026.04）

更多经历见 [Experience]({{ site.url }}/experiences/)，简历见 [CV（PDF）]({{ site.owner.cv }})。

---

## 联系方式

* 邮箱：[hongjip2@illinois.edu](mailto:hongjip2@illinois.edu) · [{{ site.owner.email }}](mailto:{{ site.owner.email }})
* [Google Scholar]({{ site.owner.scholar }}) · [GitHub](https://github.com/{{ site.owner.github }})
