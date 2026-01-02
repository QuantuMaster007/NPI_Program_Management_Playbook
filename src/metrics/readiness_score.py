#!/usr/bin/env python3
"""
Compute a simple readiness score from a checklist CSV.

Expected CSV:
item_id,domain,description,status
Where status is one of: done,in_progress,blocked,not_started

Outputs readiness % by domain and overall.
"""
import csv
from collections import defaultdict

WEIGHTS = {
    "done": 1.0,
    "in_progress": 0.5,
    "blocked": 0.0,
    "not_started": 0.0,
}

def main(path: str) -> None:
    sums = defaultdict(float)
    counts = defaultdict(int)
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            d = row["domain"].strip()
            s = row["status"].strip().lower()
            counts[d] += 1
            sums[d] += WEIGHTS.get(s, 0.0)

    overall_items = sum(counts.values())
    overall_score = sum(sums.values()) / overall_items if overall_items else 0.0

    print("Readiness by domain:")
    for d in sorted(counts):
        score = sums[d] / counts[d] if counts[d] else 0.0
        print(f"- {d}: {score:.0%} ({sums[d]:.1f}/{counts[d]})")
    print(f"\nOverall: {overall_score:.0%} ({sum(sums.values()):.1f}/{overall_items})")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", help="Path to readiness_checklist.csv")
    args = ap.parse_args()
    main(args.csv_path)
