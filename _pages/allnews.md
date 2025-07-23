---
title: "News"
layout: textlay
excerpt: "Human Centric ART Lab at Univerisity of Rome Tor Vergata"
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<div>
<b>{{article.emoji}} {{ article.date }}</b><br>
{{ article.headline | markdownify}}
</div>
{% endfor %}
