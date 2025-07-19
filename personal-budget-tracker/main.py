from datetime import datetime
from budget_utils import load_transactions, save_transactions, group_by_category

def add_transaction():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. food, bills, rent): ")
    amount = float(input("Enter amount: "))

    transactions = load_transactions()
    transactions.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    save_transactions(transactions)
    print("Transaction added successfully!")

def view_summary():
    transactions = load_transactions()
    if not transactions:
        print("No transactions to display.")
        return

    summary = group_by_category(transactions)
    print("\nCategory-wise totals:")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

while True:
    print("\n1. Add Transaction")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
