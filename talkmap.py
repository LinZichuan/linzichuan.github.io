#!/usr/bin/env python3
"""Generate a Leaflet cluster map from talk locations."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_TALKS_DIR = PROJECT_ROOT / "_talks"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "talkmap"
DEFAULT_USER_AGENT = "academicpages-talkmap"
LOCATION_PATTERN = re.compile(r'^location:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)


def extract_location(markdown_path: Path) -> str | None:
    match = LOCATION_PATTERN.search(markdown_path.read_text(encoding="utf-8"))
    if match:
        return match.group(1).strip()

    return None


def collect_locations(talks_dir: Path) -> list[str]:
    locations: list[str] = []
    for markdown_path in sorted(talks_dir.glob("*.md")):
        location = extract_location(markdown_path)
        if location:
            locations.append(location)

    return locations


def geocode_locations(locations: list[str], user_agent: str = DEFAULT_USER_AGENT) -> dict[str, object]:
    from geopy.geocoders import Nominatim

    geocoder = Nominatim(user_agent=user_agent)
    geocoded_locations: dict[str, object] = {}

    for location in locations:
        geocoded_location = geocoder.geocode(location)
        if geocoded_location is not None:
            geocoded_locations[location] = geocoded_location
            print(location, "\n", geocoded_location)
        else:
            print(f"WARNING: could not geocode {location}")

    return geocoded_locations


def generate_talk_map(
    talks_dir: Path = DEFAULT_TALKS_DIR,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    user_agent: str = DEFAULT_USER_AGENT,
) -> None:
    import getorg

    locations = collect_locations(talks_dir)
    location_dict = geocode_locations(locations, user_agent=user_agent)

    getorg.orgmap.create_map_obj()
    getorg.orgmap.output_html_cluster_map(
        location_dict,
        folder_name=str(output_dir),
        hashed_usernames=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--talks-dir", type=Path, default=DEFAULT_TALKS_DIR, help="Directory containing talk markdown")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for generated map files")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="Nominatim user agent")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generate_talk_map(args.talks_dir, args.output_dir, args.user_agent)


if __name__ == "__main__":
    main()
