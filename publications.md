---
layout: default
title: Publications
permalink: /publications/
---

# Publications

See also [Google Scholar](https://scholar.google.com/citations?user=2bcbKU0AAAAJ)

{% assign publications = site.data.publications | sort: "year" | reverse %}
{% assign groups = publications | group_by: "year" %}
{% for group in groups %}
  {% assign year_items = group.items | reverse %}
  <section class="year-group">
    <h2 class="year-heading">{{ group.name }}</h2>
    <div class="publication-list">
      {% for pub in year_items %}
        <article id="{{ pub.id }}" class="publication publication-rich">
          <p class="publication-type">{{ pub.type | default: "Publication" }}</p>
          <h3>{{ pub.title }}</h3>
          <p class="muted publication-meta">
            {{ pub.authors }}{% if pub.venue %}. <span>{{ pub.venue }}</span>{% endif %}
          </p>
          <div class="publication-links">
            {% if pub.abstract and pub.abstract != "" %}
            <button type="button" class="publication-abstract-btn" data-pub-id="{{ pub.id }}">
              <span class="iconify" data-icon="mdi:text-box-outline" aria-hidden="true"></span> Abstract
            </button>
            <div id="abstract-source-{{ pub.id }}" class="pub-abstract-source" hidden>
              <span data-title>{{ pub.title }}</span>
              <div data-body>{{ pub.abstract }}</div>
            </div>
            {% endif %}
            {% if pub.link %}<a href="{{ pub.link }}"><span class="iconify" data-icon="mdi:file-document-outline" aria-hidden="true"></span> Article</a>{% endif %}
            {% if pub.pdf %}<a href="{{ pub.pdf }}"><span class="iconify" data-icon="mdi:file-pdf-box" aria-hidden="true"></span> PDF</a>{% endif %}
            {% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}"><span class="iconify" data-icon="mdi:link-variant" aria-hidden="true"></span> DOI</a>{% endif %}
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
{% endfor %}

<dialog id="pub-abstract-dialog" class="pub-abstract-dialog" aria-labelledby="pub-abstract-dialog-title">
  <div class="pub-abstract-dialog-inner">
    <header class="pub-abstract-dialog-header">
      <h3 id="pub-abstract-dialog-title" class="pub-abstract-dialog-title"></h3>
      <button type="button" class="pub-abstract-close" aria-label="Close abstract">
        <span class="iconify" data-icon="mdi:close" aria-hidden="true"></span>
      </button>
    </header>
    <div id="pub-abstract-dialog-body" class="pub-abstract-dialog-body"></div>
  </div>
</dialog>

<script>
  (function () {
    var dialog = document.getElementById("pub-abstract-dialog");
    if (!dialog) return;

    var titleEl = document.getElementById("pub-abstract-dialog-title");
    var bodyEl = document.getElementById("pub-abstract-dialog-body");
    var closeBtn = dialog.querySelector(".pub-abstract-close");

    function openAbstract(pubId) {
      var source = document.getElementById("abstract-source-" + pubId);
      if (!source) return;
      var title = source.querySelector("[data-title]");
      var body = source.querySelector("[data-body]");
      if (!title || !body) return;
      titleEl.textContent = title.textContent;
      bodyEl.textContent = body.textContent;
      bodyEl.scrollTop = 0;
      dialog.showModal();
      bodyEl.scrollTop = 0;
    }

    document.querySelectorAll(".publication-abstract-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        openAbstract(btn.getAttribute("data-pub-id"));
      });
    });

    closeBtn.addEventListener("click", function () {
      dialog.close();
    });

    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) {
        dialog.close();
      }
    });

    dialog.addEventListener("close", function () {
      bodyEl.scrollTop = 0;
    });
  })();
</script>
