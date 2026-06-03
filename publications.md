---
layout: default
title: Publications
permalink: /publications/
---

# Publications

{% assign publications = site.data.publications | sort: "year" | reverse %}
{% assign groups = publications | group_by: "year" %}
{% for group in groups %}
  {% assign year_items = group.items | reverse %}
  <section class="year-group">
    <h2 class="year-heading">{{ group.name }}</h2>
    <div class="publication-list">
      {% for pub in year_items %}
        <article class="publication publication-rich">
          <p class="publication-type">{{ pub.type | default: "Publication" }}</p>
          <h3>{{ pub.title }}</h3>
          <p class="muted publication-meta">
            {{ pub.authors }}{% if pub.venue %}. <span>{{ pub.venue }}</span>{% endif %}
          </p>
          <div class="publication-links">
            {% if pub.link %}<a href="{{ pub.link }}"><span class="iconify" data-icon="mdi:file-document-outline" aria-hidden="true"></span> Article</a>{% endif %}
            {% if pub.pdf %}<a href="{{ pub.pdf }}"><span class="iconify" data-icon="mdi:file-pdf-box" aria-hidden="true"></span> PDF</a>{% endif %}
            {% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}"><span class="iconify" data-icon="mdi:link-variant" aria-hidden="true"></span> DOI</a>{% endif %}
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
{% endfor %}
