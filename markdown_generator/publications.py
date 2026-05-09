#!/usr/bin/env python3
"""Generate publication pages from ``publications.tsv``."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from .generator_utils import has_text, html_escape, read_tsv, require_fields, write_markdown
except ImportError:  # pragma: no cover - supports running this file directly.
    from generator_utils import has_text, html_escape, read_tsv, require_fields, write_markdown


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "publications.tsv"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "_publications"
REQUIRED_FIELDS = ("pub_date", "title", "venue", "citation", "url_slug")


def build_markdown(publication: dict[str, str]) -> tuple[str, str]:
    pub_date = publication["pub_date"].strip()
    title = publication["title"].strip()
    url_slug = publication["url_slug"].strip()
    html_filename = f"{pub_date}-{url_slug}"
    md_filename = f"{html_filename}.md"

    lines = [
        "---",
        f'title: "{html_escape(title)}"',
        "collection: publications",
        f"permalink: /publication/{html_filename}",
    ]

    if has_text(publication.get("excerpt"), min_length=5):
        lines.append(f"excerpt: '{html_escape(publication.get('excerpt'))}'")

    lines.extend(
        [
            f"date: {pub_date}",
            f"venue: '{html_escape(publication.get('venue'))}'",
        ]
    )

    if has_text(publication.get("paper_url"), min_length=5):
        lines.append(f"paperurl: '{publication['paper_url'].strip()}'")

    lines.extend(
        [
            f"citation: '{html_escape(publication.get('citation'))}'",
            "---",
        ]
    )

    body: list[str] = []
    if has_text(publication.get("excerpt"), min_length=5):
        body.append(html_escape(publication.get("excerpt")))

    if has_text(publication.get("paper_url"), min_length=5):
        body.append(f"[Download paper here]({publication['paper_url'].strip()})")

    body.append(f"Recommended citation: {publication['citation'].strip()}")

    return md_filename, "\n".join(lines) + "\n" + "\n\n".join(body)


def generate_publications(input_path: Path = DEFAULT_INPUT, output_dir: Path = DEFAULT_OUTPUT) -> list[Path]:
    written_paths: list[Path] = []
    for row_number, publication in enumerate(read_tsv(input_path), start=2):
        require_fields(publication, REQUIRED_FIELDS, row_number)
        filename, markdown = build_markdown(publication)
        written_paths.append(write_markdown(output_dir, filename, markdown))

    return written_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to publications TSV")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Directory for generated markdown")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    written_paths = generate_publications(args.input, args.output_dir)
    for path in written_paths:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
