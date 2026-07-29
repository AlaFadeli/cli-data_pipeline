from pipeline import reader
from pipeline.transformer import parse_numeric, filter_by, add_column
from pipeline.analyzer import total_revenue, revenue_by, summary
from pipeline.writer import print_table, write_csv, write_json
from pipeline.decorators import timer, log_calls


class Pipeline:
    def __init__(self):
        self.rows = []

    def load(self, filepath):
        self.rows = reader.read_csv(filepath)
        return self

    def parse_numbers(self):
        self.rows = parse_numeric(self.rows)
        return self

    def filter(self, key, value):
        self.rows = filter_by(self.rows, key, value)
        return self

    def enrich(self, name, func):
        self.rows = add_column(self.rows, name, func)
        return self

    def report(self, col="revenue", qty_col=None):
        result = summary(self.rows, col, qty_col)
        print(result)
        return self

    def top(self, n, col="revenue"):
        top_rows = sorted(self.rows, key=lambda r: r[col], reverse=True)[:n]
        print_table(top_rows, n)
        return self

    def show(self, n=10):
        print_table(self.rows, n)
        return self

    def save_json(self, filepath):
        write_json(self.rows, filepath)
        return self

    def save_csv(self, filepath):
        write_csv(self.rows, filepath)
        return self
