from __future__ import annotations

import shutil
import sys
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_DESTINATION = ROOT / ".test-site"


def entry_text(
    *,
    published: date,
    slug: str,
    section: str,
    section_slug: str,
    youtube_id: str | None = None,
) -> str:
    title = slug.replace("-", " ").title()
    primary_source = (
        f"https://www.youtube.com/watch?v={youtube_id}"
        if youtube_id
        else "https://example.com/source"
    )
    lines = [
        "---",
        f'title: "{title}"',
        f"date: {published.isoformat()} 08:00:00 +0700",
        f"section: {section}",
        f"section_slug: {section_slug}",
        f'description: "Rendered fixture for {title}."',
        'read_time: "2 min"',
        f"primary_source: {primary_source}",
    ]
    if youtube_id:
        lines.append(f"youtube_id: {youtube_id}")
    lines.extend(
        [
            "signal:",
            '  - "First signal"',
            '  - "Second signal"',
            '  - "Third signal"',
            "---",
            f"Rendered body for {title}.",
            "",
            "## Sources",
            "",
            f"- [Primary source]({primary_source})",
            "",
        ]
    )
    return "\n".join(lines)


def write_entry(
    destination: Path,
    *,
    published: date,
    slug: str,
    section: str,
    section_slug: str,
    youtube_id: str | None = None,
) -> None:
    filename = f"{published.isoformat()}-{slug}.md"
    (destination / "_entries" / filename).write_text(
        entry_text(
            published=published,
            slug=slug,
            section=section,
            section_slug=section_slug,
            youtube_id=youtube_id,
        ),
        encoding="utf-8",
    )


def build_fixture(destination: Path) -> None:
    resolved = destination.resolve()
    if resolved != ALLOWED_DESTINATION.resolve():
        raise SystemExit("destination_must_be_repo_test_site")
    if resolved.exists():
        shutil.rmtree(resolved)
    resolved.mkdir()
    for name in ("_config.yml", "index.html", "archive.html", "feed.xml"):
        shutil.copy2(ROOT / name, resolved / name)
    for name in ("_includes", "_layouts", "assets"):
        shutil.copytree(ROOT / name, resolved / name)
    (resolved / "_entries").mkdir()

    recurring = (
        (date(2026, 5, 10), "daily-10", "Daily News", "daily-news"),
        (date(2026, 5, 9), "morning-09", "Morning Brief", "morning-brief"),
        (date(2026, 5, 6), "daily-06", "Daily News", "daily-news"),
        (date(2026, 5, 5), "morning-05", "Morning Brief", "morning-brief"),
        (date(2025, 12, 1), "daily-old", "Daily News", "daily-news"),
    )
    for published, slug, section, section_slug in recurring:
        write_entry(
            resolved,
            published=published,
            slug=slug,
            section=section,
            section_slug=section_slug,
        )

    for index in range(17):
        write_entry(
            resolved,
            published=date(2026, 4, 30) - timedelta(days=index),
            slug=f"research-summary-{index:02d}",
            section="Research Summary",
            section_slug="research-summary",
            youtube_id="qyPCVqFUyDo" if index == 0 else None,
        )
    for index in range(16):
        write_entry(
            resolved,
            published=date(2026, 3, 31) - timedelta(days=index),
            slug=f"deep-research-{index:02d}",
            section="Deep Research",
            section_slug="deep-research",
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: build_render_fixture.py .test-site")
    build_fixture(ROOT / sys.argv[1])
