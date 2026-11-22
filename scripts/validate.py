#!/usr/bin/env python3
"""Validate the TOEFL 2026 Public Data CSVs.

Checks: header matches the expected columns, every row has the right number
of fields, dates are YYYY-MM-DD, source URLs start with http(s), numeric
score fields parse as numbers when present, requirement_type is one of the
allowed values, and the ETS lower bounds in score-conversion.csv match the
published table. Run from the repo root:  python3 scripts/validate.py
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_TYPES = {"minimum", "recommended", "competitive", "conditional",
                 "middle-50%", "acceptable-range", "none", "unknown"}
ETS_LOWER_BOUNDS = [114, 107, 95, 86, 72, 58, 44, 34, 24, 12, 0]

errors = []


def check_number(value, field, where):
    if value == "":
        return
    try:
        float(value)
    except ValueError:
        errors.append(f"{where}: {field}={value!r} is not a number")


def check_date(value, field, where):
    if value == "":
        errors.append(f"{where}: {field} is empty")
    elif not DATE_RE.match(value):
        errors.append(f"{where}: {field}={value!r} is not YYYY-MM-DD")


def check_url(value, field, where):
    if not value.startswith(("http://", "https://")):
        errors.append(f"{where}: {field}={value!r} is not a URL")


def validate_score_conversion(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 11:
        errors.append(f"{path.name}: expected 11 rows, got {len(rows)}")
    for i, r in enumerate(rows, start=2):
        where = f"{path.name}:{i}"
        if r["total_old_min_ets"] == "":
            errors.append(f"{where}: total_old_min_ets is empty")
        elif int(float(r["total_old_min_ets"])) != ETS_LOWER_BOUNDS[i - 2]:
            errors.append(f"{where}: total_old_min_ets={r['total_old_min_ets']} "
                          f"!= ETS lower bound {ETS_LOWER_BOUNDS[i - 2]}")
        for field in ("band_1_6", "reading_old_min", "reading_old_max",
                      "listening_old_min", "listening_old_max",
                      "speaking_old_min", "speaking_old_max",
                      "writing_old_min", "writing_old_max",
                      "total_old_max_derived",
                      "total_old_midpoint_comparable",
                      "ets_recommended_for_old_requirement"):
            check_number(r[field], field, where)
        check_url(r["source_url"], "source_url", where)
        check_date(r["source_accessed_date"], "source_accessed_date", where)


def validate_universities(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 71:
        errors.append(f"{path.name}: expected 71 rows, got {len(rows)}")
    numeric = ("toefl_old_overall_min_as_published",
               "toefl_old_section_min_reading",
               "toefl_old_section_min_listening",
               "toefl_old_section_min_speaking",
               "toefl_old_section_min_writing",
               "toefl_new_overall_min_as_published",
               "toefl_new_section_min_reading",
               "toefl_new_section_min_listening",
               "toefl_new_section_min_speaking",
               "toefl_new_section_min_writing",
               "toefl_new_overall_converted_via_ets")
    for i, r in enumerate(rows, start=2):
        where = f"{path.name}:{i} ({r.get('university_name_en')})"
        for field in numeric:
            check_number(r[field], field, where)
        if r["requirement_type"] not in ALLOWED_TYPES:
            errors.append(f"{where}: requirement_type={r['requirement_type']!r} "
                          f"not in {sorted(ALLOWED_TYPES)}")
        if r["accepts_mybest"] not in ("yes", "no", "unknown"):
            errors.append(f"{where}: accepts_mybest={r['accepts_mybest']!r}")
        check_url(r["source_url"], "source_url", where)
        check_date(r["source_accessed_date"], "source_accessed_date", where)
        check_date(r["last_verified_date"], "last_verified_date", where)
        if r["level"] not in ("undergraduate", "graduate"):
            errors.append(f"{where}: level={r['level']!r}")


def validate_di_codes(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if rows:
        errors.append(f"{path.name}: expected 0 rows (collecting), "
                      f"got {len(rows)}")


def main():
    validate_score_conversion(ROOT / "data" / "score-conversion.csv")
    validate_universities(ROOT / "data" / "universities.csv")
    validate_di_codes(ROOT / "data" / "di-codes.csv")
    if errors:
        print(f"FAILED: {len(errors)} error(s)")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: all CSVs valid "
          "(score-conversion 11 rows, universities 71 rows, di-codes 0 rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
