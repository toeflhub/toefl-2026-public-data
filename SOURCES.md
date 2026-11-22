# Sources

## ETS (official, read 2026-11-19)

- Score scale and concordance table (test-taker page):
  <https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html>
- Score scale update for institutions (same table, updated 2026-01-23):
  <https://toeflaccess.ets.org/help/en/articles/11758616-toefl-ibt-score-scale-update-what-you-need-to-know>
- Score scale, CEFR comparison and institution guidance:
  <https://www.ets.org/toefl/institutions/ibt/score-scale-update.html>
- TOEFL iBT content (task types):
  <https://www.ets.org/toefl/test-takers/ibt/about/content.html>
- Destinations Search (DI code lookup):
  <https://www.ets.org/toefl/test-takers/ibt/where-to-study/destinations-search.html>
- Score report request form (DI / department code instructions):
  <https://www.ets.org/s/toefl/pdf/iBT_ASR_form.pdf>

## Universities

Every row in `data/universities.csv` cites the exact university admissions
page it was read from (`source_url`), checked 2026-11-19. No aggregator,
forum post, or agent summary is used as a source. Rows whose source could
not be opened and read in full were excluded — 19 such rows are held back
and are not in this release.

## Method (summary)

1. **Only public pages.** University admissions pages and ETS pages. No
   logged-in content, no purchased databases.
2. **Every row has a source.** `source_url` (exact page, not just a domain)
   and `source_accessed_date`. A row without a source does not enter the file.
3. **Published vs derived, kept apart.** `*_as_published` columns hold the
   school's own numbers verbatim. `toefl_new_overall_converted_via_ets`
   holds an ETS-interval derivation only where the school published old
   scores alone — and it is labeled as a derivation, never as the school's
   requirement.
4. **Levels are separate.** Undergraduate / graduate / specific-program
   rows are separate; one school's undergraduate line is never applied to
   its graduate programs.
5. **Requirement type is recorded.** `minimum` / `recommended` /
   `competitive` / `conditional` / `middle-50%` / `none` / `unknown` — a
   competitive range is never written as a minimum.
6. **Re-check cycle.** Rows are re-checked quarterly; ETS table changes
   trigger an immediate update. Out-of-date rows are marked `stale`, never
   silently deleted.

See [data/data-dictionary.md](data/data-dictionary.md) for field definitions.
