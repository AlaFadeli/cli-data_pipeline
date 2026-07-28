from collections import defaultdict


# Uses a generator to sum all values in a column
def total_revenue(rows, col):
    total = sum((r[col] for r in rows))
    return total


# Group by group_key, accumulate col values, return sorted desc
def revenue_by(rows, group_key, col):
    groups = defaultdict(float)
    for r in rows:
        groups[r[group_key]] += r[col]
    return sorted(groups.items(), key=lambda x: x[1], reverse=True)


def summary(rows, col):
    length = len(rows)
    total = sum((r[col] for r in rows))
    total_units_sold = sum((r["quantity"] for r in rows))
    summary = {
        "total_rows": length,
        "total_revenue": total,
        "avg_revenue": total / length if length else 0,
        "max_revenue": max((r[col] for r in rows)),
        "min_revenue": min((r[col] for r in rows)),
        "total_units_sold": total_units_sold,
        "avg_units_per_sale": total_units_sold / length if length else 0,
    }
    return summary
