---
layout: default
title: Past seminars
description: Archive of past GRS seminars, thesis defences, candidature reviews, and special sessions.
---

<div class="page-header">
  <h1>Past seminars</h1>
  <p>Archive of completed events. Times are Adelaide local (ACST/ACDT).</p>
</div>

<nav class="type-nav" aria-label="Seminar types">
  <a href="#all">All past</a>
  {% for type_pair in site.seminar_types %}
  <a href="#{{ type_pair[0] }}">{{ type_pair[1].label }}</a>
  {% endfor %}
</nav>

<section class="section" id="all">
  <h2>All past seminars</h2>
  {% include seminar-list.html section="past" %}
</section>

{% for type_pair in site.seminar_types %}
  {% assign type_id = type_pair[0] %}
  {% assign type_info = type_pair[1] %}
<section class="section" id="{{ type_id }}">
  <h2>{{ type_info.label }}</h2>
  {% include seminar-list.html section="past" type_filter=type_id %}
</section>
{% endfor %}
