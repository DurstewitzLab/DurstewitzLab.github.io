#!/usr/bin/env python3
"""Convert a BibTeX file into Jekyll-friendly YAML publications data."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def _split_top_level_commas(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    in_quote = False
    quote_char = ""

    for ch in text:
        if in_quote:
            current.append(ch)
            if ch == quote_char:
                in_quote = False
            continue

        if ch in {'"', "{", "'"}:
            if ch in {'"', "'"}:
                in_quote = True
                quote_char = ch
            elif ch == "{":
                depth += 1
            current.append(ch)
            continue

        if ch == "}":
            depth = max(0, depth - 1)
            current.append(ch)
            continue

        if ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
            continue

        current.append(ch)

    if current:
        parts.append("".join(current).strip())
    return parts


def _strip_wrapping(value: str) -> str:
    value = value.strip()
    if (value.startswith("{") and value.endswith("}")) or (
        value.startswith('"') and value.endswith('"')
    ):
        return value[1:-1].strip()
    return value


def parse_bibtex(content: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    pattern = re.compile(
        r"@(?P<type>\w+)\s*\{\s*(?P<id>[^,\s]+)\s*,\s*(?P<body>.*?)\n\}",
        re.DOTALL | re.IGNORECASE,
    )

    for match in pattern.finditer(content):
        entry_type = match.group("type").strip()
        entry_id = match.group("id").strip()
        body = match.group("body")

        fields: dict[str, str] = {"id": entry_id, "type": entry_type.title()}
        for part in _split_top_level_commas(body):
            if "=" not in part:
                continue
            key, raw_value = part.split("=", 1)
            fields[key.strip().lower()] = _strip_wrapping(raw_value)

        if "author" in fields:
            fields["authors"] = fields.pop("author")
        if "journal" in fields and "venue" not in fields:
            fields["venue"] = fields["journal"]
        if "booktitle" in fields and "venue" not in fields:
            fields["venue"] = fields["booktitle"]
        if "url" in fields and "link" not in fields:
            fields["link"] = fields["url"]

        entries.append(fields)

    return entries


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def entries_to_yaml(entries: list[dict[str, str]]) -> str:
    lines: list[str] = []
    preferred = ("id", "type", "title", "authors", "year", "venue", "link", "pdf", "doi")

    for entry in entries:
        lines.append("- id: " + _yaml_quote(entry.get("id", "")))
        for key in preferred[1:]:
            if key in entry and entry[key]:
                lines.append(f"  {key}: {_yaml_quote(entry[key])}")
        for key, value in sorted(entry.items()):
            if key in preferred or not value:
                continue
            lines.append(f"  {key}: {_yaml_quote(value)}")
    return "\n".join(lines) + ("\n" if lines else "")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bibtex", nargs="?", default="_data/publications.bib")
    parser.add_argument("yaml", nargs="?", default="_data/publications.yml")
    args = parser.parse_args()

    bib_path = Path(args.bibtex)
    yaml_path = Path(args.yaml)
    content = bib_path.read_text(encoding="utf-8")
    entries = parse_bibtex(content)
    yaml_path.write_text(entries_to_yaml(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {yaml_path}")


if __name__ == "__main__":
    main()
