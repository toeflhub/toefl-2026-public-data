# Changelog

## v2026.11 — draft, not yet released (files prepared 2026-11-20)

- `data/score-conversion.csv`: 11 rows — the full ETS 1–6 vs 0–120 concordance table, with per-section old-scale ranges, derived upper bounds (marked as derived), interval midpoints, and ETS's institution recommendations for old requirements 100 / 90 / 80 / 70. Source checked 2026-11-19.
- `data/universities.csv`: 53 verified rows across 24 universities — TOEFL requirements as published on each university's own admissions pages, checked 2026-11-19. School-published values and ETS-interval derivations are separate columns.
- `data/di-codes.csv`: header only, 0 rows — collection in progress. No rows are fabricated to fill the file.
- Docs: README (EN + zh-CN), SOURCES.md, data-dictionary.md, LICENSE (MIT, scripts) + LICENSE-DATA.md (CC BY 4.0, data), CITATION.cff, scripts/validate.py.

## v2026.11 — update 2026-11-20 (still draft, not yet released)

- `data/universities.csv`: 53 → 70 rows. Of the 19 pending rows, 18 were verified against the universities' own pages on 2026-11-20 and 17 were merged (rows 54–70). The Georgia Tech 2024-2025 archived-catalog row was verified but NOT merged — it is superseded by the current-catalog row (new scale ≥ 4.5). NYU SPS undergraduate was verified later the same day via the live browser (old 100 / new 5, no section minimums, "Minimum Recommended Scores") and merged as row 71, so all 19 pending rows are now resolved and the file holds 71 rows.
- New `requirement_type` value: `acceptable-range` (University of Michigan undergraduate — a range of acceptable scores, not a minimum).
- One row (Boston University, College of Communication) is the first with `accepts_mybest=yes`, verified on the university's own page.

**Not yet done:** no GitHub account or repository has been created. The repository name (`toeflhub/toefl-2026-public-data`) and the GitHub organization name are placeholders pending confirmation. GitHub Pages is not yet enabled.
