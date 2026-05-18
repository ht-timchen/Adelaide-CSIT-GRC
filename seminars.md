---
layout: default
title: Seminars
description: Upcoming and past HDR seminars, thesis defences, candidature reviews, and special sessions.
---

<div class="page-header">
  <h1>Seminar calendar</h1>
  <p>Browse upcoming and past events by type. Times are Adelaide local (ACST/ACDT).</p>
</div>

<nav class="type-nav" aria-label="Seminar types">
  <a href="#upcoming">All upcoming</a>
  <a href="#candidature_review">Candidature review</a>
  <a href="#thesis_defence">Thesis defence</a>
  <a href="#hdr_seminar">HDR seminar</a>
  <a href="#special">Special session</a>
  <a href="#past">Past seminars</a>
</nav>

<section class="section" id="upcoming">
  <h2>Upcoming seminars</h2>
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

<section class="section" id="past">
  <h2>Past seminars</h2>
  {% include seminar-list.html section="past" %}
</section>
