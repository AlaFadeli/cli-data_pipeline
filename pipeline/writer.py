import csv
import json


# Print clean alligned table of data
def print_table(rows, max_rows):
    maxs = {key: max(len(key), max(len(str(r[key])) for r in rows)) for key in rows[0]}
    sep = "-+-".join("-" * maxs[k] for k in rows[0])

    print(" | ".join(h.ljust(maxs[h]) for h in rows[0]))
    print(sep)
    for r in rows[:max_rows]:
        print(" | ".join(str(r[h]).ljust(maxs[h]) for h in rows[0]))


# Transform the edited dict back to csv
def write_csv(rows, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# Save data as json
def write_json(rows, filepath):
    with open(filepath, "w") as f:
        json.dump(rows, f, indent=2)
