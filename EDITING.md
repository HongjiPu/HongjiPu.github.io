# 编辑指南 / Editing Guide

网站的**内容**和**样式**是分开的。日常更新只需要改 `_data/` 下的 YAML 文件和几个
Markdown 页面 —— 不用碰 HTML 或 CSS。

---

## 1. 改内容 —— 改这几个文件就够了

| 想改什么 | 改哪个文件 |
| --- | --- |
| **首页大图上方的滚动卡片** | `_data/featured.yml` |
| **News 消息栏** | `_data/news.yml` |
| **Publications 出版物栏** | `_data/publications.yml` |
| **Research 两个板块 / 模块 / 项目** | `_data/research.yml` |
| 首页 About / Education / Research Interests | `index.md` |
| 首页大图上的标题和副标题 | `index.md` 最上面的 front matter |
| Experience 经历 | `experiences.md` |
| Academic 学术服务 | `academic.md` |
| Hobbies | `hobbies.md` |
| 中文页 | `cn.md` |
| 姓名、邮箱、社交链接、导航栏 | `_config.yml` |

---

## 2. News 消息栏

`_data/news.yml`，**最新的放最上面**：

```yaml
- date: "2026.07"
  icon: "🎉"
  text: >
    <a href="https://arxiv.org/abs/xxxx" target="_blank">论文标题</a> 被
    <strong>NeurIPS 2026</strong> 接收！一句话说明。
```

- `date` 会自动加上方括号显示成 `[2026.07]`
- `icon` 可留空。常用：🎉 录用 · 🚀 发布 · 📌 其他 · 🏆 获奖
- `text` 里可以直接写 HTML：`<a>` 链接、`<strong>` 加粗、`<em>` 斜体
- 消息多了会在框内滚动，不会把页面撑长

### 给消息配图（可选）

把图片放进 `images/news/` 目录，然后加三个字段：

```yaml
- date: "2026.07"
  icon: "🎉"
  image: /images/news/paper-2026.jpg    # 图片路径
  image_alt: "论文示意图"                # 替代文字，可选
  url: "https://arxiv.org/abs/xxxx"      # 点图跳转，可选（外链自动开新标签页）
  text: >
    论文标题被 <strong>NeurIPS 2026</strong> 接收！
```

- **不写 `image` 就是纯文字条目**，两种可以混着排
- 图片会按 **4:3** 裁成缩略图，建议用横图、短边不小于 400px
- 鼠标悬停时图片会轻微放大
- `images/news/` 里的 `sample-*.jpg` 是占位图，换成你自己的之后可以删掉

---

## 2.5 首页大图上方的滚动卡片

`_data/featured.yml`，像麦肯锡首页那样一格一格陈列你想优先展示的东西：

```yaml
cards:
  - eyebrow: "Research"        # 顶部小标签
    title: "卡片标题，一到两行最好看"
    meta: "底部小字（方向 / 日期 / 状态）"   # 可选
    url: /research/foundations/              # 可选，不填就是纯展示
```

- 每 5 秒自动向左轮播一张，**鼠标放上去会暂停**，移开继续
- 也可以直接用鼠标横向拖、按右上角箭头、点下面的小横条、或用键盘左右方向键
- 手机上箭头自动隐藏，直接手指滑动
- 屏幕高度小于 620px 时自动隐藏，把空间让给大标题
- 不想要这个区域：把 `cards:` 下面全删掉，只留 `cards: []`

---

## 3. Publications 出版物栏

`_data/publications.yml`。顺序随便写，页面会按 `year` / `month` 自动排序。

```yaml
highlight_authors:     # 你名字的各种写法，命中任意一个就自动加粗
  - "Hongji Pu"
  - "H Pu"

categories:            # 筛选按钮，按这里的顺序显示
  - Efficient Agent Infrastructure
  - Reliability

items:
  - title: "论文标题"
    authors: ["H Pu", "合作者"]          # 用哪种写法都行，见 highlight_authors
    venue: "arXiv:2605.00180, 2026"
    year: 2026
    month: 5                             # 可选，用于同年内排序
    category: "Reinforcement Learning"   # 必须是上面 categories 里的一个
    extra_categories: ["Multi-Agent AI"] # 可选，让它同时出现在别的方向下
    selected: true                       # 可选，出现在默认的 "show selected"
    links:
      - name: Paper                      # Paper / Code / Demo / Slides 各有图标
        url: "https://..."
      - name: Code
        url: "https://github.com/..."
```

页面顶部三个切换：`show selected` / `show all by date` / `show all by topic`，
外加搜索框和方向筛选，全部自动生成。

---

## 4. Research 两个板块

`_data/research.yml` 的结构是 **pillar（板块）→ module（模块）→ project（项目）**：

```yaml
pillars:
  - key: applications        # 不要改 key，页面靠它取数据
    number: "01"
    title: "AI Applications"
    tagline: "首页板块上显示的一句话"
    blurb: "板块页面顶部的一段话"
    url: /research/applications/
    modules:
      - name: "Finance AI"
        summary: "这个模块在做什么"
        projects:
          - name: "Finance Router"
            summary: "一两句话介绍"
            status: "In progress"        # 可选的小徽章
            venue: "NeurIPS 2026"        # 可选
            tags: ["Routing", "Finance"] # 可选
            links:
              - name: Paper
                url: "#"                 # 还没有就先留 "#"
              - name: Code
                url: "#"
```

- 加一个新模块 = 在 `modules:` 下加一块；加一篇 paper = 在 `projects:` 下加一块
- 两个 pillar 页面分别是 `research/applications.md` 和 `research/foundations.md`，
  它们只有一行 `include`，正常不用改

### 这份数据在三个地方复用

改一次 `_data/research.yml`，三处会同步更新：

| 位置 | 用的组件 | 样子 |
| --- | --- | --- |
| 首页 **04 — Publication** | `research-mini.html` | 两个紧凑的深色小卡片 |
| `/research/` 页面 | `research-split.html` | 两个整幅大面板 |
| 两个 pillar 页面 | `research-pillar.html` | 模块 + 项目卡片全展开 |

想在首页再加一个整幅深色版本（原来那个），在 `_layouts/home.html` 的
`{% comment %}` 那一段位置贴回这几行：

```liquid
<section class="band band--navy">
  <div class="shell">
    <span class="eyebrow eyebrow--light">Research</span>
    <h2 style="color:#fff;margin:0 0 10px;">Two pillars</h2>
    <p style="max-width:56ch;margin:0 0 44px;">你的介绍语</p>
    {% include research-split.html %}
  </div>
</section>
```

---

## 5. 首页大图区

在 `index.md` 最上面：

```yaml
hero_title: "Hongji Pu"
hero_lede: "大标题下面那句话"
hero_meta:                    # 底部三个带小方块的标签
  - "Financial Engineering · UIUC"
  - "Quantitative Research"
quote: "深色引言条里的那句话"   # 删掉这两行就不显示引言条
quote_label: "Point of view"
```

背景图是根目录的 `hero.jpg`，换图直接替换这个文件，或在 `_config.yml` 里
改 `owner.hero_img`。**建议换成一张横向、中间偏暗、和你研究方向相关的大图** ——
现在的 `hero.jpg`（打铁）和 `bio_photo.jpg`（猫）大概率是模板自带的占位图。

---

## 6. 导航栏和个人信息

`_config.yml`：

```yaml
owner:
  name: Hongji Pu
  role: MSFE · UIUC        # 侧栏名字下面那行
  email: ...
  github: ...              # 填了才会显示对应图标
  linkedin: ...
  scholar: ...             # 填完整 URL
  cv: /file/CV.pdf         # 取消注释就会显示 CV 链接

links:                     # 顶部导航栏，顺序即显示顺序
  - title: About Me
    url: /
```

---

## 7. 改样式

所有样式集中在 `assets/css/theme.css`，最上面是一组变量：

```css
--navy:  #051C2C;   /* 主色，深海军蓝 */
--blue:  #2251FF;   /* 强调色 */
--cyan:  #00A9F4;   /* 次强调色 */
--serif: ...        /* 标题字体 */
--sans:  ...        /* 正文字体 */
```

改这几个变量就能整站换色，不用逐条改。

---

## 8. 本地预览

```bash
bundle exec jekyll serve
```

然后打开 http://localhost:4000 。直接 push 到 GitHub 也会自动构建。

---

## 备份

改版前的 layouts / includes / index.md / publications.md 都在
`backup/pre-redesign/`。
