# Durstewitz Lab Website (Jekyll)

Static site for the Theoretical NeuroScience / Durstewitz Lab.

## Requirements

- Ruby + Jekyll (global install is fine: `jekyll build`)

## Build & preview

```bash
jekyll build
jekyll serve
```

Restart `jekyll serve` after editing `_config.yml`.

### GitHub Pages (`username.github.io/repository/`)

For a **project site**, set `baseurl` to **`"/repository-name"`** (path only, with a leading slash) and set `url` to **`"https://USERNAME.github.io"`**. If `baseurl` is wrong or empty, the HTML loads but `/assets/css/style.css` resolves to the wrong host path and styles disappear.

For a **user or organization site** served from the special `USERNAME.github.io` repository at the domain root, use `baseurl: ""` and set `url` to your Pages URL (or custom domain).

## Content

| File | Purpose |
|------|---------|
| `_config.yml` | Site title, `url`, and **`baseurl`** (see GitHub Pages below) |
| `_data/site.yml` | Organization, contact, group photo |
| `_data/team.yml` | Team members |
| `_data/teaching.yml` | Lectures (`latest_iteration`, outline, image) |
| `_data/publications.bib` | BibTeX source |
| `_data/publications.yml` | Generated publication list |

### Publications from BibTeX

```bash
python3 bibtex_to_yaml.py
# or: python3 bibtex_to_yaml.py _data/publications.bib _data/publications.yml
```

### Team photos

- Group photo: `_data/site.yml` → `group_photo`, `group_photo_alt`, `group_photo_y`
- Portraits: per member in `_data/team.yml` → `portrait: /assets/images/team/name.jpg`
- Missing/broken portraits fall back to name initials automatically

### Teaching

Edit `_data/teaching.yml`. Cards sort by `latest_iteration` (e.g. `Summer Term 2026`, `Winter Term 2025/26`).

## Pages

- `/` — Home
- `/team/` — Team
- `/publications/` — Publications
- `/materials/` — Downloads & materials
- `/teaching/` — Lecture recordings
- `/contact/` — Contact

## Images

Place assets under `assets/images/` (e.g. `group_photo_2025.jpg`, `team/daniel.jpg`).
