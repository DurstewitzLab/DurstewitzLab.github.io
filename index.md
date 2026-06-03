---
layout: default
title: Home
permalink: /
---

<section class="hero">
  <p class="kicker">Durstewitz Lab</p>
  <h1>Theoretical Neuroscience</h1>
  <p class="lead">
    This website is currently under heavy development. For now, please refer to the <a href="{{ '/legacy-website/' | relative_url}}">legacy website</a>.
  </p>
  <p class="hero-actions">
    <a class="button button-primary" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="button button-secondary" href="{{ '/team/' | relative_url }}">Team</a>
  </p>
</section>

{% if site.data.site.group_photo and site.data.site.group_photo != "" %}
<figure class="group-photo" style="--group-photo-y: {{ site.data.site.group_photo_y | default: 'center' }};">
  <img src="{{ site.data.site.group_photo | relative_url }}" alt="{{ site.data.site.group_photo_alt | default: 'Lab group photo' }}" loading="lazy" />
</figure>
{% endif %}