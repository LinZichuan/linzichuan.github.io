"""Shared helpers for academicpages markdown generators."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
}


def clean_text(value: object) -> str:
    """Return a stripped string while treating missing values as empty."""
    if value is None:
        return ""

    text = str(value).strip()
    if text.lower() == "nan":
        return ""

    return text


def has_text(value: object, min_length: int = 0) -> bool:
    return len(clean_text(value)) > min_length


def html_escape(value: object) -> str:
    """Escape text for YAML fields that are later rendered as HTML."""
    return "".join(HTML_ESCAPE_TABLE.get(char, char) for char in clean_text(value))


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file, delimiter="\t"))


def require_fields(row: dict[str, str], fields: Iterable[str], row_number: int) -> None:
    missing = [field for field in fields if not has_text(row.get(field))]
    if missing:
        names = ", ".join(missing)
        raise ValueError(f"Row {row_number} is missing required field(s): {names}")


def safe_output_path(output_dir: Path, filename: str) -> Path:
    return output_dir / Path(filename).name


def write_markdown(output_dir: Path, filename: str, content: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = safe_output_path(output_dir, filename)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return path
