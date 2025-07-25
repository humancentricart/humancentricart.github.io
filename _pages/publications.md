---
title: "Human Centric ART Lab - Publications"
layout: gridlay
excerpt: "Human Centric ART Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Group highlights - ACL 2025

**At the end of this page, you can find the [full list of publications and patents](#full-list-of-publications).**

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit><a href="{{ publi.url }}">{{ publi.title }}</a></pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.abstract }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p>{{ publi.booktitle +' '+ publi.year}}</p>
  <!-- <p><strong><a href="{{ publi.url }}">{{ publi.link.display }}</a></strong></p> -->
  <!-- <p class="text-danger"><strong> {{ publi.news1 }}</strong></p> -->
  <!-- <p> {{ publi.news2 }}</p> -->
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


<!--## Patents
<em>Milan P Allan, S Gröblacher, RA Norte, M Leeuwenhoek</em><br />Novel atomic force microscopy probes with phononic crystals<br /> PCT/NL20-20/050797 (2020)

<em>Milan P Allan</em><br /> Methods of manufacturing superconductor and phononic elements <br /> <a href="https://patents.google.com/patent/US10439125B2/en?inventor=Milan+ALLAN&oq=inventor:(Milan+ALLAN)">US10439125B2 (2016)</a>
-->

## Full List of publications

{% for publi in site.data.publist %}
  <!-- <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a> -->
  <b>{{ publi.year }} </b><br />
  <em>{{ publi.authors }} </em><br />
  <a href="{{ publi.url }}">{{ publi.title }}</a><br />
  {{ publi.booktitle +' '+ publi.journal +' '+ publi.organization +' '+ publi.publisher + ' ' + publi.volume }}
{% endfor %}
