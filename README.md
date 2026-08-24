# Curious Signal

Morning audio, useful research, and the sources behind both.

This is a static GitHub Pages archive. Each edition is a Markdown file in
`_entries/` with a small public metadata header. Audio lives under `audio/`.
GitHub Pages turns those files into a bounded recent homepage, a complete
year-and-month archive, and individual listening
pages using the shared layout in `_layouts/entry.html`.

The homepage shows Daily News and Morning Brief from the latest five-day window
anchored to the newest recurring edition, plus the newest 15 entries in each
Research section. The complete `/archive/` supports section filters and text
search. `feed.xml` publishes
the same collection as an RSS feed, including MP3 enclosures when audio exists.
The homepage “Latest listen” player automatically uses the newest published
Morning Brief, so publishing the daily entry and MP3 advances the player without
a separate featured-content step.

## Publish contract

An entry may include:

- title, date, section, description, and reading time
- three concise `signal` takeaways
- one finished MP3 and its duration
- the cleaned written brief or transcript
- public source links
- a validated `youtube_id` when a Research edition's primary source is a
  supported YouTube video

An entry must not include raw workflow manifests, local paths, prompts, model
paths, voice IDs, job IDs, API keys, private notes, WAV files, or partial audio.

If a recording is incomplete, omit the `audio` field. The site will label the
page as a text edition.

When `youtube_id` is present, the entry layout constructs a lazy-loaded player
on YouTube's privacy-enhanced host and retains the primary-source fallback link.
Source content never supplies iframe HTML or an embed URL.

Current public sections are Daily News, Morning Brief, Research Summary, and
Deep Research.

## Local preview

GitHub Pages builds this with Jekyll. With Ruby and Bundler already available:

```sh
bundle exec jekyll serve
```

The public production URL is configured for:

`https://bumblebee-agent.github.io/curious-signal/`
