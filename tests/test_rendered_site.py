from __future__ import annotations

import os
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


SITE_ENV = os.environ.get("JEKYLL_SITE_DIR")


def cards(html: str) -> list[tuple[str, str, str]]:
    matches = re.findall(
        r'<article class="entry-card" data-section="([^"]+)"[^>]*>'
        r'.*?<h3><a href="([^"]+)">([^<]+)</a></h3>.*?</article>',
        html,
        re.DOTALL,
    )
    return [(section, href, title) for section, href, title in matches]


@unittest.skipUnless(SITE_ENV, "requires a rendered Jekyll site")
class RenderedSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.site = Path(SITE_ENV or "")
        cls.home = (cls.site / "index.html").read_text(encoding="utf-8")
        cls.archive = (cls.site / "archive" / "index.html").read_text(encoding="utf-8")

    def test_homepage_has_exact_recurring_window_and_research_limits(self) -> None:
        homepage_cards = cards(self.home)
        counts = {
            section: sum(card[0] == section for card in homepage_cards)
            for section in {card[0] for card in homepage_cards}
        }
        self.assertEqual(
            counts,
            {
                "daily-news": 2,
                "morning-brief": 1,
                "research-summary": 15,
                "deep-research": 15,
            },
        )
        titles = {card[2] for card in homepage_cards}
        self.assertNotIn("Morning 05", titles)
        self.assertNotIn("Daily Old", titles)
        self.assertNotIn("Research Summary 15", titles)
        self.assertNotIn("Research Summary 16", titles)
        self.assertNotIn("Deep Research 15", titles)

    def test_archive_is_complete_newest_first_and_links_to_rendered_entries(self) -> None:
        archive_cards = cards(self.archive)
        self.assertEqual(len(archive_cards), 38)
        self.assertEqual(
            re.findall(r'<h2 class="archive-year-title"[^>]*>([^<]+)</h2>', self.archive),
            ["2026", "2025"],
        )
        self.assertEqual(
            re.findall(r'<h3 class="archive-group-title"[^>]*>([^<]+)</h3>', self.archive),
            ["May", "April", "March", "December"],
        )
        self.assertEqual(archive_cards[0][2], "Daily 10")
        self.assertEqual(archive_cards[-1][2], "Daily Old")
        for _, href, _ in archive_cards:
            relative = href.removeprefix("/curious-signal/").strip("/")
            self.assertTrue((self.site / relative / "index.html").is_file(), href)
        self.assertIn('id="archive-search"', self.archive)
        self.assertIn('id="archive-status" aria-live="polite"', self.archive)

    def test_research_video_is_rendered_from_identity_with_fallback(self) -> None:
        pages = []
        for path in (self.site / "listen").glob("*/index.html"):
            text = path.read_text(encoding="utf-8")
            if "youtube-nocookie.com/embed/" in text:
                pages.append(text)
        self.assertEqual(len(pages), 1)
        page = pages[0]
        self.assertIn(
            'src="https://www.youtube-nocookie.com/embed/qyPCVqFUyDo"', page
        )
        self.assertIn('loading="lazy"', page)
        self.assertIn('title="Watch Research Summary 00 on YouTube"', page)
        self.assertIn("allowfullscreen", page)
        self.assertIn(
            'href="https://www.youtube.com/watch?v=qyPCVqFUyDo"', page
        )
        self.assertNotIn("<script>qyPCVqFUyDo", page)

    def test_feed_limit_and_existing_permalink_contract_remain_stable(self) -> None:
        feed = ET.parse(self.site / "feed.xml")
        items = feed.findall("./channel/item")
        self.assertEqual(len(items), 25)
        self.assertEqual(items[0].findtext("title"), "Daily 10")
        links = [item.findtext("link") or "" for item in items]
        self.assertTrue(all("/curious-signal/listen/" in link for link in links))


if __name__ == "__main__":
    unittest.main()
