# CLI Data Pipeline

A command-line sales data pipeline built to apply Python fundamentals: modules, CSV parsing, generators, decorators, classes, and CLI tooling.

## Download & Setup

```bash
git clone https://github.com/AlaFadeli/cli-data_pipeline.git
cd cli-data_pipeline
python3 main.py data/sample_sales.csv --report
```

Requires Python 3.7+ (standard library only — no pip install needed).

### Adapt to your own CSV

Edit the config block at the top of `main.py`:

```python
COMPUTED_COL = "revenue"
COMPUTED_FUNC = lambda r: r["quantity"] * r["unit_price"]
ANALYZE_COL = "revenue"
```

Change `COMPUTED_COL` and `ANALYZE_COL` to match your column names,
and update `COMPUTED_FUNC` to compute your derived value.

## Usage

```bash
python3 main.py data/sample_sales.csv --report --top 3 --show 5
```

### Options

| Flag | Description |
|---|---|
| `file` | Path to CSV (required, positional) |
| `--filter-key` | Column to filter on |
| `--filter-value` | Value to match |
| `--top` | Show top N rows by revenue |
| `--report` | Print summary (total, avg, max, min revenue + units) |
| `--show` | Print table with N rows (default 10) |
| `--save-json` | Save output to JSON file |
| `--save-csv` | Save output to CSV file |

### Examples

```bash
# Full report with top sellers
python3 main.py data/sample_sales.csv --report --top 3

# Filter by region, show results, save
python3 main.py data/sample_sales.csv --filter-key region --filter-value North --show 5 --save-json north_only.json
```

## Pipeline steps

1. **Load** — read CSV into `list[dict]`
2. **Parse** — convert strings to numbers
3. **Enrich** — add computed columns (e.g. `revenue = quantity × unit_price`)
4. **Filter** — keep matching rows
5. **Report** — print summary statistics
6. **Show/Top** — print formatted table
7. **Save** — export to CSV or JSON

## Modules

| Module | Responsibility |
|---|---|
| `pipeline/reader.py` | CSV input (`read_csv`, `read_csv_lazy`) |
| `pipeline/transformer.py` | Data transformation (`parse_numeric`, `filter_by`, `add_column`) |
| `pipeline/analyzer.py` | Aggregation (`total_revenue`, `revenue_by`, `summary`) |
| `pipeline/writer.py` | Output (`print_table`, `write_csv`, `write_json`) |
| `pipeline/decorators.py` | Utility decorators (`timer`, `log_calls`) |
| `pipeline/core.py` | `Pipeline` class — chains all steps |
