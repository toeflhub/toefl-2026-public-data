# Data dictionary

General rules: UTF-8, LF line endings, first row is the header, English
snake_case field names. Dates are `YYYY-MM-DD`. Scores are numbers, never
text like "about 90". When a value is unknown, leave the field empty — do
not write "unknown" into a numeric column. Every row must have a source
URL and a check date.

## Which columns are what

- **ETS original**: `total_old_min_ets` in `score-conversion.csv` — the
  lower bound ETS itself publishes (114+, 107+, 95+, …).
- **Derived from ETS**: `total_old_max_derived` and
  `total_old_midpoint_comparable` in `score-conversion.csv`, and
  `toefl_new_overall_converted_via_ets` in `universities.csv`. Upper bound
  = next band's lower bound minus 1; midpoint = middle of the band's
  interval. Derivations are labeled as such in `notes` and must never be
  presented as ETS's or a university's own words.
- **School-published**: all `*_as_published` columns in
  `universities.csv` — the university's own numbers, verbatim.

## `data/score-conversion.csv` (11 rows)

| Field | Definition | Format / values |
|---|---|---|
| `band_1_6` | New 1–6 band | 1 to 6 in 0.5 steps |
| `cefr` | CEFR level for the band | A1, A2, B1, B2, C1, C2 |
| `reading_old_min` / `reading_old_max` | Old-scale Reading range for the band | 0–30, or empty if not published |
| `listening_old_min` / `listening_old_max` | Old-scale Listening range | 0–30 |
| `speaking_old_min` / `speaking_old_max` | Old-scale Speaking range | 0–30 |
| `writing_old_min` / `writing_old_max` | Old-scale Writing range | 0–30 |
| `total_old_min_ets` | Old-scale total lower bound, ETS original | 0–120 |
| `total_old_max_derived` | Old-scale total upper bound, derived | 0–120 |
| `total_old_midpoint_comparable` | Interval midpoint (the comparable overall score on a score report) | 0–120, may be x.5 |
| `ets_recommended_for_old_requirement` | ETS's recommended new requirement for an old requirement | Only 100 → 5, 90 → 4.5, 80 → 4, 70 → 3.5; otherwise empty — do not extrapolate |
| `source_url` | ETS page the row was read from | URL |
| `source_accessed_date` | Date the source was read | YYYY-MM-DD |
| `notes` | What is ETS original vs derived, and any rounding caveat | Text |

## `data/universities.csv` (71 rows; one row = one university × one level/program)

| Field | Definition | Format / values |
|---|---|---|
| `university_name_en` | University name in English | Text |
| `university_name_zh` | University name in Chinese | Text |
| `country` | Country | USA, Canada, … |
| `region_state` | State / province | e.g. MA, CA, ON, BC |
| `level` | Applicant level | `undergraduate` / `graduate` |
| `program_college` | School / college / program the row applies to | Text; "Undergraduate (all)" / "Graduate School" when school-wide |
| `toefl_old_overall_min_as_published` | Old-scale (0–120) overall minimum as published | Number, or empty |
| `toefl_old_section_min_reading` / `listening` / `speaking` / `writing` | Old-scale section minimums as published | 0–30, or empty |
| `toefl_new_overall_min_as_published` | New-scale (1–6) overall minimum as published | 1–6, or empty |
| `toefl_new_section_min_reading` / `listening` / `speaking` / `writing` | New-scale section minimums as published | 1–6, or empty |
| `toefl_new_overall_converted_via_ets` | New-scale overall derived from an old-only publication via the ETS interval table | 1–6, or empty; only filled where the school published old scores alone; labeled as a derivation in `notes` |
| `requirement_type` | What kind of number this is | `minimum` / `recommended` / `competitive` / `conditional` / `middle-50%` / `acceptable-range` / `none` / `unknown` |
| `accepts_mybest` | Whether MyBest scores are accepted | `yes` / `no` / `unknown` (all rows are currently `unknown` — not verified) |
| `requirement_as_published` | Short verbatim quote of the school's wording | Text |
| `source_url` | Exact university page the row was read from | URL |
| `source_accessed_date` | Date the source was read | YYYY-MM-DD |
| `last_verified_date` | Date the row was last re-checked | YYYY-MM-DD |
| `notes` | Secondary values (e.g. a higher ThM line, a recommended score next to a minimum), tier details, cutoff-date quirks | Text |

`requirement_type` values:

- `minimum` — the school states a minimum.
- `recommended` — the school recommends a score; not a hard cutoff.
- `competitive` — the figure describes competitive / successful applicants, not a cutoff.
- `conditional` — the figure is a conditional-admission line.
- `middle-50%` — the figure is the middle 50% range of admitted students.
- `acceptable-range` — the figure is a range of acceptable scores, not a minimum.
- `none` — the school publishes no minimum (or explicitly requires no exam).
- `unknown` — the type could not be determined from the source.

## `data/di-codes.csv` (0 rows — collecting)

| Field | Definition | Format / values |
|---|---|---|
| `institution_name_en` / `institution_name_zh` | Institution name | Text |
| `country` / `city_state` | Location | Text |
| `di_code` | Designated Institution code, exactly as published | Text — keep leading zeros (e.g. 0980); do not store as a number |
| `department_code_example` | A department code the institution publishes | Only if published on the source page; otherwise empty |
| `department_name` | Department the example code belongs to | Text |
| `level` | `undergraduate` / `graduate` / `both` | Text |
| `source_url` / `source_accessed_date` / `last_verified_date` | As above | URL / YYYY-MM-DD |
| `notes` | Notes | Text |
