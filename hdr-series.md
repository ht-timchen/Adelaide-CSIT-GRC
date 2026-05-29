---
layout: default
title: HDR series
description: Tentative 2026 HDR Seminar Series program — fortnightly sessions for CSIT graduate research students.
---

<div class="page-header">
  <h1>{{ site.hdr_series.title }}</h1>
  <p>{{ site.hdr_series.description }}</p>
  <p class="page-header__meta">
    Sessions are booked at <strong>North Terrace (CE)</strong> and <strong>Machine Learning Building (ML)</strong> — times and rooms vary by week (see table). See
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
