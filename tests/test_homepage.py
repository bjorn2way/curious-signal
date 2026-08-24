import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HomepageLatestListenTests(unittest.TestCase):
    def test_homepage_shows_only_the_bounded_recent_collection(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn("recurring_cutoff_epoch", homepage)
        self.assertIn("minus: 345600", homepage)
        self.assertIn("{% break %}", homepage)
        self.assertNotIn("where_exp", homepage)
        self.assertIn(
            '"research-summary|Research Summary,deep-research|Deep Research"',
            homepage,
        )
        self.assertEqual(homepage.count("limit: 15"), 1)
        self.assertIn("href=\"{{ '/archive/' | relative_url }}\"", homepage)
        self.assertNotIn('id="archive-search"', homepage)

    def test_latest_listen_uses_newest_morning_brief(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn(
            "{% assign featured = sorted_entries | where: 'section_slug', "
            "'morning-brief' | first %}",
            homepage,
        )
        self.assertNotIn("where: 'featured', true", homepage)

    def test_newest_morning_brief_has_playable_audio_metadata(self) -> None:
        morning_briefs: list[tuple[str, dict[str, str]]] = []
        for path in (ROOT / "_entries").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            front_matter = text.split("\n---\n", 1)[0].removeprefix("---\n")
            metadata = {
                key.strip(): value.strip().strip('"')
                for line in front_matter.splitlines()
                if ":" in line
                for key, value in [line.split(":", 1)]
            }
            if metadata.get("section_slug") == "morning-brief":
                morning_briefs.append((metadata["date"], metadata))

        self.assertTrue(morning_briefs)
        _, newest = max(morning_briefs, key=lambda item: item[0])
        self.assertTrue(newest.get("audio", "").endswith(".mp3"))
        self.assertTrue(newest.get("duration"))

    def test_archive_cards_render_bounded_excerpts(self) -> None:
        card = (ROOT / "_includes" / "entry-card.html").read_text(encoding="utf-8")
        stylesheet = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")

        self.assertIn(
            "{{ include.entry.description | strip_newlines | truncatewords: 36 }}",
            card,
        )
        self.assertIn("-webkit-line-clamp: 3", stylesheet)

    def test_july_16_morning_brief_description_is_a_real_snippet(self) -> None:
        entry = (
            ROOT / "_entries" / "2026-07-16-morning-brief-2026-07-16.md"
        ).read_text(encoding="utf-8")
        description_line = next(
            line for line in entry.splitlines() if line.startswith("description: ")
        )
        description = json.loads(description_line.removeprefix("description: "))

        expected_excerpt = (
            "xAI released Grok Build under Apache 2.0, but Hacker News users express "
            "severe skepticism due to alleged data exfiltration and lack of commit history."
        )
        self.assertEqual(description, expected_excerpt)
        self.assertLessEqual(len(description), 240)
        self.assertIn(f'  - "{expected_excerpt}"', entry)

    def test_july_16_morning_brief_has_truthful_grouped_provenance(self) -> None:
        entry = (
            ROOT / "_entries" / "2026-07-16-morning-brief-2026-07-16.md"
        ).read_text(encoding="utf-8")

        self.assertIn("*Bumblebee original.*", entry)
        for heading in ("### News", "### Weather"):
            self.assertIn(heading, entry)
        self.assertNotIn("### Daily Focus", entry)
        self.assertIn("*Derived from today's News.*", entry)
        self.assertIn("https://github.com/xai-org/grok-build", entry)
        self.assertIn("https://developer.puter.com/labs/firefox-wasm/", entry)
        self.assertIn("https://api.open-meteo.com/v1/forecast", entry)
        self.assertIn("https://air-quality-api.open-meteo.com/v1/air-quality", entry)
        self.assertNotIn("([News]", entry)
        self.assertNotIn("([Daily Focus]", entry)
        self.assertNotIn("([Weather]", entry)


if __name__ == "__main__":
    unittest.main()
