---
layout: default
title: Teaching
permalink: /teaching/
---

# Teaching

<div class="teaching-cards" data-teaching-cards>
{% for lecture in site.data.teaching %}
  <section class="lecture-card" data-latest-iteration="{{ lecture.latest_iteration | default: '' | escape }}">
    {% if lecture.image and lecture.image != "" %}
      <img class="lecture-image" src="{{ lecture.image | relative_url }}" alt="{{ lecture.title }} lecture image" loading="lazy" />
    {% endif %}
    <h2>{{ lecture.title }}</h2>
    {% if lecture.latest_iteration %}
      <p class="muted lecture-meta">{{ lecture.latest_iteration }}</p>
    {% endif %}
    {% if lecture.summary %}
      <p class="muted">{{ lecture.summary }}</p>
    {% endif %}
    {% if lecture.outline %}
      <h3>Outline</h3>
      <ul>
        {% for item in lecture.outline %}
          <li>{{ item }}</li>
        {% endfor %}
      </ul>
    {% endif %}
    {% if lecture.moodle and lecture.moodle != "" %}
      <p class="lecture-links">
        <a href="{{ lecture.moodle }}">
          <span class="iconify" data-icon="mdi:school-outline" aria-hidden="true"></span>
          Link to Moodle
        </a>
      </p>
    {% endif %}
  </section>
{% endfor %}
</div>

<script>
  (function () {
    var container = document.querySelector("[data-teaching-cards]");
    if (!container) return;

    var cards = Array.prototype.slice.call(container.querySelectorAll(".lecture-card"));

    function parseIteration(value) {
      var text = (value || "").trim();
      var match = text.match(/^(Summer|Winter)\s+Term\s+(\d{4})(?:\/(\d{2}))?$/i);
      if (!match) return Number.NEGATIVE_INFINITY;

      var season = match[1].toLowerCase();
      var startYear = Number(match[2]);
      var seasonRank = season === "winter" ? 1 : 0;
      return startYear * 10 + seasonRank;
    }

    cards
      .sort(function (a, b) {
        var aKey = parseIteration(a.getAttribute("data-latest-iteration"));
        var bKey = parseIteration(b.getAttribute("data-latest-iteration"));
        return bKey - aKey;
      })
      .forEach(function (card) {
        container.appendChild(card);
      });
  })();
</script>
