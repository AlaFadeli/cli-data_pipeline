import csv


def read_csv(filepath: str):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        return rows


def read_csv_lazy(filepath: str):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        rows = (row for row in reader)
        return rows
