#!/usr/bin/env python3
"""Generate talk pages from ``talks.tsv``."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from .generator_utils import has_text, html_escape, read_tsv, require_fields, write_markdown
except ImportError:  # pragma: no cover - supports running this file directly.
    from generator_utils import has_text, html_escape, read_tsv, require_fields, write_markdown


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "talks.tsv"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "_talks"
REQUIRED_FIELDS = ("title", "url_slug", "date")


def build_markdown(talk: dict[str, str]) -> tuple[str, str]:
    date = talk["date"].strip()
    title = talk["title"].strip()
    url_slug = talk["url_slug"].strip()
    html_filename = f"{date}-{url_slug}"
    md_filename = f"{html_filename}.md"
    talk_type = talk["type"].strip() if has_text(talk.get("type"), min_length=3) else "Talk"

    lines = [
        "---",
        f'title: "{html_escape(title)}"',
        "collection: talks",
        f'type: "{html_escape(talk_type)}"',
        f"permalink: /talks/{html_filename}",
    ]

    if has_text(talk.get("venue"), min_length=3):
        lines.append(f'venue: "{html_escape(talk.get("venue"))}"')

    lines.append(f"date: {date}")

    if has_text(talk.get("location"), min_length=3):
        lines.append(f'location: "{html_escape(talk.get("location"))}"')

    lines.append("---")

    body: list[str] = []
    if has_text(talk.get("talk_url"), min_length=3):
        body.append(f"[More information here]({talk['talk_url'].strip()})")

    if has_text(talk.get("description"), min_length=3):
        body.append(html_escape(talk.get("description")))

    return md_filename, "\n".join(lines) + "\n\n" + "\n\n".join(body)


def generate_talks(input_path: Path = DEFAULT_INPUT, output_dir: Path = DEFAULT_OUTPUT) -> list[Path]:
    written_paths: list[Path] = []
    for row_number, talk in enumerate(read_tsv(input_path), start=2):
        require_fields(talk, REQUIRED_FIELDS, row_number)
        filename, markdown = build_markdown(talk)
        written_paths.append(write_markdown(output_dir, filename, markdown))

    return written_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to talks TSV")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Directory for generated markdown")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    written_paths = generate_talks(args.input, args.output_dir)
    for path in written_paths:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
