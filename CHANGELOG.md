# Changelog

## 2026-08-25 · Bounded archive and Research video

- Limited the homepage to the latest five-day recurring window and the newest
  15 entries in each Research section, while preserving the newest Morning
  Brief player.
- Added a complete `/archive/` grouped by year and month with the existing
  section filters, text search, accessible result status, and shared compact
  edition cards.
- Added responsive, lazy-loaded `youtube-nocookie.com` players for future
  Research entries carrying a validated `youtube_id`, with a normal primary
  source fallback link. Existing entries were not backfilled.

## 2026-07-16 · External link navigation

- Added one shared site-shell rule that opens external HTTP and HTTPS links in
  a new tab with `noopener noreferrer`, while same-origin, anchor, RSS, email,
  and other non-web links keep their existing navigation behavior.

## 2026-07-16

- Repaired the July 16 Morning Brief provenance display without changing its
  audio. The edition now shows the generated Bumblebee-original Morning Spark,
  grouped News and Weather sources, truthful derived-from-News attribution for
  Daily Focus, and an in-page `View sources` control instead of presenting the
  first link as the composite edition's primary source.

## 2026-07-16 · Compact archive excerpts

- Replaced the July 16 Morning Brief's accidental full-script description and
  first signal with the existing compact News bullet while retaining the full
  News text on the edition page.
- Bounded visible archive excerpts to 36 words with a three-line visual safety
  net for legacy entries.

## 2026-07-16 · Compact edition titles

- Reduced the responsive edition-page title scale so long generated headlines
  no longer dominate most of the first viewport on desktop or mobile.
- Added regression coverage for the desktop and mobile title bounds.

## 2026-07-16 · Latest Morning Brief player

- Changed the homepage “Latest listen” player to select the newest published
  Morning Brief automatically instead of relying on a manually pinned legacy
  `featured` flag.
- Added a regression test for the homepage selection rule.

## 2026-07-10 · Editorial cleanup

- Added Daily News as its own section with a complete six-minute audio edition.
- Added three-point “In brief” summaries to every entry.
- Standardized article structure and reduced duplicated deep-research sections.
- Replaced internal source labels with readable inline citations.
- Added expandable evidence notes, section filters, archive search, full dates,
  and an RSS feed with audio enclosures.

## 2026-07-10

- Created the first public Curious Signal edition for GitHub Pages.
- Added one morning brief, two research summaries, and two deep research briefs.
- Published four complete MP3 files; kept the incomplete ChatGPT Work recording
  out of the archive and marked that page as a text edition.
- Added a shared entry template so future publishing can be reduced to one
  Markdown file plus an optional MP3.
