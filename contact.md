---
layout: default
title: Contact
permalink: /contact/
---

# Contact

<span class="iconify" data-icon="mdi:email-outline" aria-hidden="true"></span> **Email:**
<br>
[{{ site.data.site.contact.email }}](mailto:{{ site.data.site.contact.email }})
<br><br>
<span class="iconify" data-icon="mdi:map-marker-outline" aria-hidden="true"></span> **Address:**<br>
{% assign address_parts = site.data.site.contact.address | split: ',' -%}
{%- for part in address_parts -%}
{{- part | strip -}}{%- unless forloop.last -%}<br>{%- endunless -%}
{%- endfor %}