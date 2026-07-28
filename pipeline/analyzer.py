from collections import defaultdict


# Uses a generator to sum all revenue
def total_revenue(rows):
    total_revenue = sum((r["revenue"] for r in rows))
    return total_revenue


# Sort by group_key
def revenue_by(rows, group_key):
    groups = defaultdict(float)
    for r in rows:
        groups[r[group_key]] += r["revenue"]
    return sorted(groups.items(), key=lambda x: x[1])
