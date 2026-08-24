from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ArchivePageTests(unittest.TestCase):
    def test_reader_can_browse_every_edition_by_year_and_month(self) -> None:
        archive_path = ROOT / "archive.html"

        self.assertTrue(archive_path.exists(), "the complete archive route is missing")
        archive = archive_path.read_text(encoding="utf-8")
        self.assertIn("permalink: /archive/", archive)
        self.assertIn("site.entries | sort: 'date' | reverse", archive)
        self.assertIn("group_by_exp", archive)
        self.assertIn("entry.date | date: '%Y'", archive)
        self.assertIn("entry.date | date: '%Y-%m'", archive)

    def test_archive_is_the_complete_browsing_destination(self) -> None:
        shell = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
        entry = (ROOT / "_layouts" / "entry.html").read_text(encoding="utf-8")
        archive = (ROOT / "archive.html").read_text(encoding="utf-8")

        self.assertIn("{{ '/archive/' | relative_url }}", shell)
        self.assertIn("{{ '/archive/' | relative_url }}", entry)
        self.assertIn('id="archive-search"', archive)
        self.assertIn('id="archive-status" aria-live="polite"', archive)

    def test_archive_controls_hide_empty_groups_and_fit_mobile_width(self) -> None:
        script = (ROOT / "assets" / "js" / "archive.js").read_text(encoding="utf-8")
        stylesheet = (ROOT / "assets" / "css" / "style.css").read_text(
            encoding="utf-8"
        )

        self.assertIn('group.hidden = !group.querySelector(".entry-card:not([hidden])")', script)
        self.assertIn('`${visibleCount} ${visibleCount === 1 ? "edition" : "editions"} found`', script)
        self.assertIn(".archive-search { min-width: 0; width: 100%; }", stylesheet)
        self.assertIn(
            ".entry-card { grid-template-columns: 52px minmax(0, 1fr);",
            stylesheet,
        )


if __name__ == "__main__":
    unittest.main()
