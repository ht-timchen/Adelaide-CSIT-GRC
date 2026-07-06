---
layout: default
title: Home
---

<div class="page-header">
  <h1>Graduate Research — CSIT</h1>
  <p>Upcoming seminars for HDR students in the School of Computer Science and IT, Adelaide University.</p>
</div>

<section class="section">
  <h2>Coming up</h2>
  {% assign today = site.time | date: "%Y-%m-%d" %}
  {% assign sorted = site.data.seminars.seminars | sort: "date" %}
  {% assign shown = 0 %}
  <ul class="seminar-list">
  {% for seminar in sorted %}
    {% assign date_str = seminar.date | append: "" %}
    {% assign show_seminar = true %}
    {% if seminar.title contains "Student research presentation practice" %}
      {% assign show_seminar = false %}
    {% endif %}
    {% if date_str >= today and shown < 5 and show_seminar %}
      {% include seminar-card.html seminar=seminar %}
      {% assign shown = shown | plus: 1 %}
    {% endif %}
  {% endfor %}
  </ul>
  {% if shown == 0 %}
  <p class="empty-state">No upcoming seminars scheduled. Check back soon.</p>
  {% endif %}
</section>

<p class="home-links">
  <a href="{{ '/hdr-series' | relative_url }}">HDR Seminar Series 2026 (full program) →</a>
  ·
  <a href="{{ '/seminars' | relative_url }}">All upcoming seminars</a>
  ·
  <a href="{{ '/past-seminars' | relative_url }}">Past seminars</a>
</p>
