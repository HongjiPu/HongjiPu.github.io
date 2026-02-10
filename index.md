
---
layout: archive
author_profile: true
title: "Hongji Pu"   # 这是显示在大图中间的巨大名字
excerpt: "Ph.D. Student | Data Science | AI" # 这是大名字下面的小字，可以改
header:
  overlay_image: /images/home-bg.jpg  # ⚠️记得把你的高清大图命名为 home-bg.jpg 放在 images 文件夹里
  overlay_filter: 0.5 # 遮罩透明度
---

<style>
  /* 1. 让头部占满整个屏幕高度 */
  .page__hero--overlay {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 50px;
    margin-bottom: 0;
  }

  /* 2. 大标题样式 */
  .page__hero--overlay .page__title {
    font-size: 4rem;
    margin-bottom: 10px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }

  /* 3. 副标题样式 */
  .page__hero--overlay .page__lead {
    font-size: 1.5rem;
    max-width: 800px;
  }

  /* 4. 向下滚动的箭头样式 */
  .scroll-down-arrow {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 2rem;
    animation: bounce 2s infinite;
    cursor: pointer;
    opacity: 0.8;
    z-index: 10;
  }

  /* 箭头的跳动动画 */
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {transform: translateX(-50%) translateY(0);}
    40% {transform: translateX(-50%) translateY(-10px);}
    60% {transform: translateX(-50%) translateY(-5px);}
  }
  
  /* 5. 消除间隙 */
  #main { margin-top: 0 !important; }
</style>

<div class="scroll-down-arrow" onclick="window.scrollBy({top: window.innerHeight, behavior: 'smooth'});">
  ⬇
</div>

## 👨‍💻 About Me

Here is **Hongji Pu** [(Zax, 蒲洪基)](https://www.eng.cam.ac.uk/profiles/hc663).

I am currently a Data Science student at UIUC.  
*(你可以在这里多写一点简介，比如：I define myself as a...)*

---

## 🔬 Research Interests

* **Interest 1:** (e.g., Computer Vision)
* **Interest 2:** (e.g., Natural Language Processing)
* **Interest 3:** (e.g., AI for Healthcare)

*(你可以像上面这样列出你的研究方向)*

---

## 🔥 News and Updates

* **[Feb 2026]** 🎉 My personal website is online!
* **[Jan 2026]** (Add your recent news here...)

---

## 💬 Chat with me

If you are interested in my research or have any questions, feel free to contact me via email.

* **Email:** `hongjip2@gmail.com`

{% comment %}
<h3 style="margin-top: 50px;">📄 Latest Blogs</h3>
{% for post in site.posts limit:3 %}
  <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a> <small>({{ post.date | date: "%Y-%m-%d" }})</small></li>
{% endfor %}
{% endcomment %}