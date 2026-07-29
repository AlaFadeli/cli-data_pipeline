import argparse
from pipeline.core import Pipeline


# === CONFIG ===
# Change these to adapt the pipeline to a different CSV structure.
COMPUTED_COL = "revenue"         # column added by enrich (set to None to skip)
COMPUTED_FUNC = lambda r: r["quantity"] * r["unit_price"]
ANALYZE_COL = "revenue"          # column used by report / top
QTY_COL = "quantity"             # column for unit counts (set to None to skip)


parser = argparse.ArgumentParser(description="Sales data pipeline")
parser.add_argument("file", help="Path to CSV file")
parser.add_argument("--filter-key")
parser.add_argument("--filter-value")
parser.add_argument("--top", type=int)
parser.add_argument("--report", action="store_true")
parser.add_argument("--show", type=int, default=10)
parser.add_argument("--save-json")
parser.add_argument("--save-csv")

args = parser.parse_args()

p = Pipeline().load(args.file).parse_numbers()

if COMPUTED_COL:
    p.enrich(COMPUTED_COL, COMPUTED_FUNC)

if args.filter_key and args.filter_value:
    p.filter(args.filter_key, args.filter_value)
if args.report:
    p.report(ANALYZE_COL, QTY_COL)
if args.top:
    p.top(args.top, ANALYZE_COL)
if args.show:
    p.show(args.show)
if args.save_json:
    p.save_json(args.save_json)
if args.save_csv:
    p.save_csv(args.save_csv)
