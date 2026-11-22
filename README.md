# TOEFL 2026 Public Data — 1–6 Score Conversion, DI Codes & University Requirements

> Open, sourced, versioned summaries of public TOEFL information for the January 2026 TOEFL iBT format. Maintained by [ToeflHub](https://toeflhub.com/).
>
> Data: [score conversion](data/score-conversion.csv) · [DI codes](data/di-codes.csv) · [university requirements](data/universities.csv)

## What this is

A collection of public information, organized so others can cite it:

- The ETS 1–6 vs 0–120 concordance table (`data/score-conversion.csv`, 11 rows).
- TOEFL requirements published on university admissions pages (`data/universities.csv`, 71 verified rows, 24 universities, checked 2026-11-19–20).
- DI (Designated Institution) codes from ETS Destinations Search (`data/di-codes.csv`, collecting — header only for now).

Every row carries its source URL and the date it was checked. See [SOURCES.md](SOURCES.md) and [data/data-dictionary.md](data/data-dictionary.md).

## What this is not

- Not an ETS publication, not any university's official requirement, no real test questions, no admission guarantee.
- Not "official data". We are not ETS, and we claim no partnership with ETS or any university.

## Quick answers

- From January 21, 2026, TOEFL iBT scores are 1–6 in 0.5 steps. The total is the average of the four section scores, rounded to the nearest 0.5.
- ETS's recommendation to institutions (not a conversion formula for test takers): old 100 → new 5; old 90 → new 4.5; old 80 → new 4; old 70 → new 3.5.
- Transition until January 2028: score reports show the CEFR level, the 1–6 scores, and a comparable 0–120 overall score (the midpoint of the matching interval).

## Data files

| File | Rows | Last verified |
|---|---|---|
| `data/score-conversion.csv` | 11 | 2026-11-19 |
| `data/universities.csv` | 71 | 2026-11-20 |
| `data/di-codes.csv` | 0 (collecting) | — |

## How to use the conversion table

- The official table is an **interval mapping, not a point conversion**: one 1–6 band maps to a range of 0–120 scores. A total of 100 falls in band 5 (95–106); that does not mean "100 = 5.0".
- ETS's original table gives only the lower bound of each band (114+, 107+, 95+, …). The upper bounds in this file are derived (next band's lower bound minus 1) and marked as derived in the notes column.
- The comparable overall score on a score report is the midpoint of the band's interval, per ETS.

## How to cite

> Source: ToeflHub, "TOEFL 2026 Public Data", ETS concordance table, accessed 2026-11-19, https://github.com/toeflhub/toefl-2026-public-data

## Sources & methodology

See [SOURCES.md](SOURCES.md). Key rules: only public pages; every row has a source URL and check date; school-published values and ETS-interval derivations are separate columns (never mixed); rows are re-checked quarterly and marked stale when out of date.

## About ToeflHub

ToeflHub (https://toeflhub.com/) is an AI-driven TOEFL iBT mock test platform with 68 full mock tests for the 2026 format and AI scoring for Writing and Speaking. The data in this repo is free to use with attribution; the mock tests are a separate product.

## Contributing / Corrections

Found a mistake? Open an issue with the row, what's wrong, and the correct source URL. Corrections are accepted when they come with a public source — a claim without a source is not merged.

## License

- Data: [CC BY 4.0](LICENSE-DATA.md) — free to use with attribution.
- Code / scripts: [MIT](LICENSE).

## Changelog

- v2026.11 (draft, not yet released): score-conversion.csv (11 rows, ETS table), universities.csv (53 verified rows), di-codes.csv (header only, collecting). See [CHANGELOG.md](CHANGELOG.md).

## Disclaimer

Data is a summary of public information. The ETS concordance table is ETS's publication, cited here with source links; this repo claims no copyright over ETS's table itself. University requirements remain the copyright of the respective universities. Always confirm with the university's official admissions page and ETS before applying.
