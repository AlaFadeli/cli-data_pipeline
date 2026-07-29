# CLI Data Pipeline — Build Plan

## Step 1: Scaffold

```
python-programming/projects/data-pipeline/
├── data/
│   └── sample_sales.csv
├── pipeline/
│   ├── __init__.py
│   ├── reader.py
│   ├── transformer.py
│   ├── analyzer.py
│   ├── writer.py
│   ├── decorators.py
│   └── core.py
└── main.py
```

## Step 2: Dataset

`data/sample_sales.csv` — 36 rows, columns: `date,product,category,quantity,unit_price,region`

## Step 3: Reader (`pipeline/reader.py`)

- `read_csv(filepath)` → `list[dict]` using `csv.DictReader` + `list()`
- `read_csv_lazy(filepath)` → generator yielding one dict per row using `yield`

File handled with `with open(...) as f:`. Values are all strings at this stage.

## Step 4: Transformer (`pipeline/transformer.py`)

All functions take `list[dict]` and return `list[dict]`.

- `parse_numeric(rows)` — convert quantity/unit_price to float, date stays string
- `filter_by(rows, key, value)` — list comprehension with `if`
- `add_revenue(rows)` — `{**r, "revenue": r["quantity"] * r["unit_price"]}`

## Step 5: Analyzer (`pipeline/analyzer.py`)

- `total_revenue(rows)` — `sum(r["revenue"] for r in rows)` (generator expr)
- `revenue_by(rows, group_key)` — `defaultdict(float)`, accumulate, return sorted desc
- `summary(rows)` — dict with total/avg/max/min revenue, total units

## Step 6: Writer (`pipeline/writer.py`)

- `print_table(rows, max_rows=20)` — compute column widths with `max(len(...))`, print header + separator + rows
- `write_csv(rows, filepath)` — `csv.DictWriter`
- `write_json(rows, filepath)` — `json.dump`

## Step 7: Decorators (`pipeline/decorators.py`)

- `timer(func)` — `@functools.wraps`, `time.perf_counter()`, print `func.__name__` + elapsed
- `log_calls(target_list)` — factory, appends `{"name", "args", "result"}` dicts

## Step 8: Pipeline class (`pipeline/core.py`)

- `Pipeline` with `load()`, `parse_numbers()`, `filter()`, `enrich()`, `report()`, `top()`, `show()`, `save_json()`, `save_csv()`
- Each method decorated with `@timer`
- No inheritance — composition only

## Step 9: CLI (`main.py`)

- `argparse` with `file`, `--filter-key`, `--filter-value`, `--top`, `--report`, `--show`, `--save-json`, `--save-csv`
- Instantiate `Pipeline`, chain method calls

## Validation

```bash
python3 main.py data/sample_sales.csv --report --top 3 --show 5
```
