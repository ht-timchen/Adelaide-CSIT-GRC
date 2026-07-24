---
layout: default
title: GRS series
description: Tentative 2026 GRS Series program — weekly sessions for CSIT Graduate Research Students.
permalink: /grs-series/
---

<div class="page-header">
  <h1>{{ site.hdr_series.title }}</h1>
  <p>{{ site.hdr_series.description }}</p>
  <p class="page-header__meta">
    Sessions are <strong>4:00–5:00 pm</strong> (Adelaide time), at <strong>North Terrace (CE)</strong> and <strong>Mawson Lakes (ML)</strong> — rooms vary by week (see table). See
    <a href="{{ '/seminars' | relative_url }}">Upcoming seminars</a> for candidature reviews and other events.
  </p>
</div>

<section class="section">
  <h2>Program (tentative)</h2>
  {% include hdr-series-table.html %}
</section>

<section class="section">
  <h2>Session details</h2>
  {% assign series_id = site.hdr_series.id %}
  {% assign sessions = site.data.seminars.seminars | where: "series", series_id | sort: "session_number" %}
  <ul class="seminar-list">
  {% for s in sessions %}
    {% include seminar-card.html seminar=s %}
  {% endfor %}
  </ul>
</section>
