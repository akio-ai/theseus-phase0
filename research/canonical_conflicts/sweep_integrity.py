"""Canonical data-integrity sweep — measurement only, writes nothing.

Answers two questions left open by Batch 8:
  1. How many canonical cuvee names carry embedded PAIRED quote marks (family S-2)?
     Batch 7 estimated 9 from the producers seen in Batches 5-7. That was a sample.
  2. How many canonical records hold a vintage that is not a 4-digit year?
     Raised by Batch 8 (roulot-perrieres holds '-'), which asked for a DB-wide
     sweep before anyone assigns the shape a number.

Run:  python3 research/canonical_conflicts/sweep_integrity.py

This script DOES NOT modify canonical or REGISTER.md. It is evidence for an
adjudication that belongs to the CTO (D-2026-08-04-03: escalate, never resolve).
"""
import json
import re
import collections

CANONICAL = "migration/out/export/db_wine_canonical.json"


def classify_name(name):
    """Distinguish embedded quote marks (a defect) from French elision (correct).

    'Clos de l'Arlot' and "L'Esprit ..." use a legitimate apostrophe and are NOT
    S-2. Only PAIRED quote marks wrapping a segment are the defect.
    """
    n = str(name)
    if re.search(r'^".*"$', n) or re.search(r'"[^"]+"', n):
        return "paired_double"
    if re.search(r"^'.*'$", n) or re.search(r"‘[^’]+’", n):
        return "paired_single"
    if '"' in n:
        return "stray_double"
    if "'" in n or "’" in n:
        return "apostrophe_only"  # legitimate French elision - NOT a defect
    return None


def main():
    records = json.load(open(CANONICAL))
    print(f"canonical records: {len(records)}\n")

    # --- S-2: embedded quote marks in cuvee names -------------------------
    buckets = collections.defaultdict(list)
    for r in records:
        k = classify_name(r.get("name"))
        if k:
            buckets[k].append((r["id"], r["name"]))

    defect = sum(len(buckets[k]) for k in ("paired_double", "paired_single", "stray_double"))
    print("=== S-2 : embedded quote marks in cuvee names ===")
    for k in ("paired_double", "paired_single", "stray_double", "apostrophe_only"):
        if buckets[k]:
            note = "  <- legitimate French elision, NOT a defect" if k == "apostrophe_only" else ""
            print(f"  {k:<16} {len(buckets[k]):>4}{note}")
    print(f"  TRUE S-2 total: {defect} records "
          f"({defect / len(records) * 100:.1f}% of canonical)")
    print(f"  Batch 7 estimate was 9. That was a sample of the producers then researched.\n")

    # --- non-year vintages ------------------------------------------------
    bad = [r for r in records if not re.fullmatch(r"\d{4}", str(r.get("vintage", "")))]
    dist = collections.Counter(str(r.get("vintage")) for r in bad)
    emdash = [r for r in bad if str(r.get("vintage")) == "—"]
    nv_plain = dist.get("NV", 0)
    nv_structured = sum(c for v, c in dist.items() if v.startswith("NV") and v != "NV")

    print("=== vintage field : values that are not a 4-digit year ===")
    print(f"  total non-year records: {len(bad)} ({len(bad) / len(records) * 100:.1f}% of canonical)")
    print(f"    '-' (em-dash sentinel) : {len(emdash):>4}  across "
          f"{len(set(r['producer'] for r in emdash))} producers")
    print(f"    'NV' (legitimate)      : {nv_plain:>4}  <- correct for non-vintage Champagne")
    print(f"    'NV + base year' forms : {nv_structured:>4}  <- this is family V-1, not a sentinel")
    print("\n  Three DIFFERENT things share one field. Only the em-dash is a true null.")
    print("  Sample of the structured NV forms (family V-1):")
    for v, c in sorted(dist.items()):
        if v.startswith("NV") and v != "NV":
            print(f"    {v!r} x{c}")


if __name__ == "__main__":
    main()
