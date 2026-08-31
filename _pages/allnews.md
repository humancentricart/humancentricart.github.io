---
title: "News"
layout: textlay
excerpt: "Human Centric ART Lab at Univerisity of Rome Tor Vergata"
sitemap: false
permalink: /allnews.html
---

# X

<a class="twitter-timeline" href="https://x.com/HumanCentricArt?ref_src=twsrc%5Etfw">Posts by HumanCentricArt</a> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>

# News

{% for article in site.data.news %}
<div>
<b>{{article.emoji}} {{ article.date }}</b><br>
{{ article.headline | markdownify}}
</div>
{% endfor %}
