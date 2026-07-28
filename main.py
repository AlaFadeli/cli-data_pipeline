import argparse
from pipeline.core import Pipeline


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

p = Pipeline().load(args.file).parse_numbers() \
              .enrich("revenue", lambda r: r["quantity"] * r["unit_price"])

if args.filter_key and args.filter_value:
    p.filter(args.filter_key, args.filter_value)
if args.report:
    p.report()
if args.top:
    p.top(args.top)
if args.show:
    p.show(args.show)
if args.save_json:
    p.save_json(args.save_json)
if args.save_csv:
    p.save_csv(args.save_csv)
