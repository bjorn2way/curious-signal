from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class EntryLayoutTests(unittest.TestCase):
    def test_research_youtube_identity_renders_a_privacy_enhanced_player(self) -> None:
        layout = (ROOT / "_layouts" / "entry.html").read_text(encoding="utf-8")
        stylesheet = (ROOT / "assets" / "css" / "style.css").read_text(
            encoding="utf-8"
        )

        self.assertIn("{% if page.youtube_id %}", layout)
        self.assertIn("https://www.youtube-nocookie.com/embed/{{ page.youtube_id }}", layout)
        self.assertIn('loading="lazy"', layout)
        self.assertIn('title="Watch {{ page.title | escape }} on YouTube"', layout)
        self.assertIn("allowfullscreen", layout)
        self.assertIn("Watch on YouTube ↗", layout)
        self.assertIn(".video-frame { overflow: hidden; aspect-ratio: 16 / 9;", stylesheet)

    def test_entry_titles_use_compact_responsive_scale(self) -> None:
        stylesheet = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")

        self.assertIn("font-size: clamp(40px, 5vw, 58px)", stylesheet)
        self.assertIn("font-size: clamp(34px, 9vw, 40px)", stylesheet)

    def test_composite_morning_brief_links_to_grouped_sources(self) -> None:
        layout = (ROOT / "_layouts" / "entry.html").read_text(encoding="utf-8")

        self.assertIn('{% if page.section_slug == "morning-brief" %}', layout)
        self.assertIn('href="#sources">View sources ↓</a>', layout)
        self.assertIn("{% elsif page.primary_source %}", layout)
        self.assertIn("Primary source ↗", layout)

    def test_shared_shell_opens_only_external_web_links_in_new_tabs(self) -> None:
        layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
        script = (ROOT / "assets" / "js" / "external-links.js").read_text(
            encoding="utf-8"
        )

        self.assertIn("/assets/js/external-links.js", layout)
        self.assertIn("destination.origin === window.location.origin", script)
        self.assertIn("destination.protocol !== \"http:\"", script)
        self.assertIn("destination.protocol !== \"https:\"", script)
        self.assertIn('link.target = "_blank"', script)
        self.assertIn('link.relList.add("noopener", "noreferrer")', script)


if __name__ == "__main__":
    unittest.main()
