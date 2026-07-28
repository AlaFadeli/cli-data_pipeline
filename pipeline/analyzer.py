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


def summary(rows):
    length = len(rows)
    total_revenue = sum((r["revenue"] for r in rows))
    total_units_sold = sum((r["quantity"] for r in rows))
    summary = {
        "total_rows": length,
        "total_revenue": total_revenue,
        "avg_revenue": total_revenue / length,
        "max_revenue": max((r["revenue"] for r in rows)),
        "min_revenue": min((r["revenue"] for r in rows)),
        "total_units_sold": total_units_sold,
        "avg_units_per_sale": total_units_sold / length,
    }
