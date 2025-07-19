import json
import os

DATA_FILE = "transactions.json"

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_transactions(transactions):
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def group_by_category(transactions):
    category_totals = {}
    for txn in transactions:
        cat = txn["category"]
        amt = txn["amount"]
        category_totals[cat] = category_totals.get(cat, 0) + amt
    return category_totals
