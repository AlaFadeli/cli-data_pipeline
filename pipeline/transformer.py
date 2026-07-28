# Helper Function
def to_num(v):
    try:
        return float(v)
    except ValueError:
        return v


# Transform float str to float
def parse_numeric(rows):
    return [{k: to_num(v) for k, v in row.items()} for row in rows]


# Filter by value of key
def filter_by(rows, key, value):
    filtered = [row for row in rows if row[key] == value]
    return filtered


# Add column
def add_column(rows, name, func):
    return [{**r, name: func(r)} for r in rows]
