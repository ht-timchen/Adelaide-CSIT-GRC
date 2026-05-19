---
layout: default
title: Seminars
description: Upcoming HDR seminars, thesis defences, candidature reviews, and special sessions.
---

<div class="page-header">
  <h1>Upcoming seminars</h1>
  <p>Browse upcoming events by type. Times are Adelaide local (ACST/ACDT). For past events, see <a href="{{ '/past-seminars' | relative_url }}">Past seminars</a>.</p>
</div>

<nav class="type-nav" aria-label="Seminar types">
  <a href="#upcoming">All upcoming</a>
  <a href="#candidature_review">Candidature review</a>
  <a href="#thesis_defence">Thesis defence</a>
  <a href="#hdr_seminar">HDR seminar</a>
  <a href="#special">Special session</a>
</nav>

<section class="section" id="upcoming">
  <h2>All upcoming</h2>
  {% include seminar-list.html section="upcoming" %}
</section>

{% for type_pair in site.seminar_types %}
  {% assign type_id = type_pair[0] %}
  {% assign type_info = type_pair[1] %}
<section class="section" id="{{ type_id }}">
  <h2>{{ type_info.label }}</h2>
  {% include seminar-list.html section="upcoming" type_filter=type_id %}
</section>
{% endfor %}
