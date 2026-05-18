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
    {% if date_str >= today and shown < 5 %}
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
  <a href="{{ '/seminars' | relative_url }}">View all seminars and archive →</a>
</p>
