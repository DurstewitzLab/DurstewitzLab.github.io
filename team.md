---
layout: default
title: Team
permalink: /team/
---

<h1 class="team-page-title">Team</h1>

{% assign attractor_url = '/assets/images/team/attractors/lorenz.svg' | relative_url %}
{% assign ordered_groups = "Principal Investigator|Postdoctoral Researchers|PhD Candidates|Masters Students|Bachelors Students" | split: "|" %}
{% for group_name in ordered_groups %}
{% assign has_group_members = false %}
{% for m in site.data.team %}
{% assign role_lc = m.role | downcase %}
{% assign is_match = false %}
{% if group_name == "Principal Investigator" and role_lc == "principal investigator" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Postdoctoral Researchers" and role_lc contains "postdoc" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Postdoctoral Researchers" and role_lc contains "postdoctoral" %}{% assign is_match = true %}{% endif %}
{% if group_name == "PhD Candidates" and role_lc contains "phd" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Masters Students" and role_lc contains "master" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Bachelors Students" and role_lc contains "bachelor" %}{% assign is_match = true %}{% endif %}
{% if is_match %}{% assign has_group_members = true %}{% endif %}
{% endfor %}
{% if has_group_members %}
<section class="team-role-group">
  <h2>{{ group_name }}</h2>
  <div class="team-grid">
{% for member in site.data.team %}
{% assign role_lc = member.role | downcase %}
{% assign is_match = false %}
{% if group_name == "Principal Investigator" and role_lc == "principal investigator" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Postdoctoral Researchers" and role_lc contains "postdoc" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Postdoctoral Researchers" and role_lc contains "postdoctoral" %}{% assign is_match = true %}{% endif %}
{% if group_name == "PhD Candidates" and role_lc contains "phd" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Masters Students" and role_lc contains "master" %}{% assign is_match = true %}{% endif %}
{% if group_name == "Bachelors Students" and role_lc contains "bachelor" %}{% assign is_match = true %}{% endif %}
{% unless is_match %}{% continue %}{% endunless %}
{% assign name_parts = member.name | split: " " %}
{% assign last_name = name_parts | last %}
    <article class="team-card" data-sort-last="{{ last_name | downcase }}" data-sort-name="{{ member.name | downcase }}">
      <div class="team-portrait-wrap">
{% if member.portrait %}
          <img class="portrait" src="{{ member.portrait.path | relative_url }}" alt="Portrait of {{ member.name }}" loading="lazy" style="object-position: {{ member.portrait.x | default: 50 }}% {{ member.portrait.y | default: 50 }}%;" onerror="this.style.display='none';this.nextElementSibling.style.display='grid';" />
          <div class="avatar" aria-hidden="true" style="display: none;"><span class="attractor-avatar" aria-hidden="true" style="-webkit-mask-image:url('{{ attractor_url }}');mask-image:url('{{ attractor_url }}')"></span></div>
{% else %}
          <div class="avatar" aria-hidden="true"><span class="attractor-avatar" aria-hidden="true" style="-webkit-mask-image:url('{{ attractor_url }}');mask-image:url('{{ attractor_url }}')"></span></div>
{% endif %}
      </div>
      <h3 class="team-name">{{ member.name }}</h3>
    </article>
{% endfor %}
  </div>
</section>
{% endif %}
{% endfor %}

{% assign roles = site.data.team | map: "role" | uniq %}
{% for role in roles %}
{% assign role_lc = role | downcase %}
{% if role_lc == "principal investigator" or role_lc contains "postdoc" or role_lc contains "postdoctoral" or role_lc contains "phd" or role_lc contains "master" or role_lc contains "bachelor" or role_lc == "alumni" %}
{% continue %}
{% endif %}
<section class="team-role-group">
{% assign role_heading = role %}
{% assign role_lc_heading = role | downcase %}
{% unless role_lc_heading == "principal investigator" or role_lc_heading == "alumni" %}
  {% assign last_char = role_heading | slice: -1, 1 %}
  {% unless last_char == "s" %}
    {% assign role_heading = role_heading | append: "s" %}
  {% endunless %}
{% endunless %}
  <h2>{{ role_heading }}</h2>
  <div class="team-grid">
{% assign members = site.data.team | where: "role", role %}
{% for member in members %}
{% assign name_parts = member.name | split: " " %}
{% assign last_name = name_parts | last %}
    <article class="team-card" data-sort-last="{{ last_name | downcase }}" data-sort-name="{{ member.name | downcase }}">
      <div class="team-portrait-wrap">
{% if member.portrait %}
          <img class="portrait" src="{{ member.portrait.path | relative_url }}" alt="Portrait of {{ member.name }}" loading="lazy" style="object-position: {{ member.portrait.x | default: 50 }}% {{ member.portrait.y | default: 50 }}%;" onerror="this.style.display='none';this.nextElementSibling.style.display='grid';" />
          <div class="avatar" aria-hidden="true" style="display: none;"><span class="attractor-avatar" aria-hidden="true" style="-webkit-mask-image:url('{{ attractor_url }}');mask-image:url('{{ attractor_url }}')"></span></div>
{% else %}
          <div class="avatar" aria-hidden="true"><span class="attractor-avatar" aria-hidden="true" style="-webkit-mask-image:url('{{ attractor_url }}');mask-image:url('{{ attractor_url }}')"></span></div>
{% endif %}
      </div>
      <h3 class="team-name">{{ member.name }}</h3>
    </article>
{% endfor %}
  </div>
</section>
{% endfor %}

{% assign alumni_members = site.data.team | where: "role", "Alumni" %}
{% if alumni_members.size > 0 %}
<section class="team-role-group">
  <h2>Alumni</h2>
  <div class="team-grid alumni-grid">
{% for member in alumni_members %}
{% assign name_parts = member.name | split: " " %}
{% assign last_name = name_parts | last %}
{% if member.website %}
    <a class="alumni-card" href="{{ member.website }}" data-sort-last="{{ last_name | downcase }}" data-sort-name="{{ member.name | downcase }}">
      {{ member.name }}
    </a>
{% else %}
    <article class="alumni-card" data-sort-last="{{ last_name | downcase }}" data-sort-name="{{ member.name | downcase }}">
      {{ member.name }}
    </article>
{% endif %}
{% endfor %}
  </div>
</section>
{% endif %}

<script>
  (function () {
    var grids = document.querySelectorAll(".team-grid");
    grids.forEach(function (grid) {
      var cards = Array.from(grid.querySelectorAll(".team-card, .alumni-card"));
      cards.sort(function (a, b) {
        var aLast = a.getAttribute("data-sort-last") || "";
        var bLast = b.getAttribute("data-sort-last") || "";
        var byLast = aLast.localeCompare(bLast, undefined, { sensitivity: "base" });
        if (byLast !== 0) return byLast;
        var aName = a.getAttribute("data-sort-name") || "";
        var bName = b.getAttribute("data-sort-name") || "";
        return aName.localeCompare(bName, undefined, { sensitivity: "base" });
      });
      cards.forEach(function (card) {
        grid.appendChild(card);
      });
    });
  })();
</script>
