"""
Task 3: Practical Implementation Project
Project: Personal Expense Tracker

A command-line application to record expenses, list them, summarize spending,
and save/load records using a CSV file. Uses only Python's standard library.
"""

import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"
FIELDS = ["date", "category", "amount", "note"]


def load_expenses(filename=DATA_FILE):
    """Load expense records from a CSV file; return an empty list if absent."""
    if not os.path.exists(filename):
        return []
    expenses = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expenses.append({
                        "date": row["date"],
                        "category": row["category"],
                        "amount": float(row["amount"]),
                        "note": row.get("note", ""),
                    })
                except (KeyError, TypeError, ValueError):
                    # Skip malformed rows rather than stopping the application.
                    continue
    except OSError as error:
        print(f"Could not read expense file: {error}")
    return expenses


def save_expenses(expenses, filename=DATA_FILE):
    """Save all expense records to a CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            for expense in expenses:
                writer.writerow({
                    "date": expense["date"],
                    "category": expense["category"],
                    "amount": f'{expense["amount"]:.2f}',
                    "note": expense["note"],
                })
        return True
    except OSError as error:
        print(f"Could not save expenses: {error}")
        return False


def add_expense(expenses):
    """Collect and validate details for a new expense."""
    category = input("Category (e.g., Food, Travel, Books): ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    while True:
        try:
            amount = float(input("Amount (greater than 0): "))
            if amount > 0:
                break
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    note = input("Note (optional): ").strip()
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "note": note,
    }
    expenses.append(expense)
    if save_expenses(expenses):
        print("Expense saved successfully.")
    else:
        print("Expense added for this session, but could not be saved to disk.")


def list_expenses(expenses):
    """Display all expense records."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense History ---")
    print(f'{"No.":<5} {"Date":<12} {"Category":<18} {"Amount":>10}  Note')
    print("-" * 65)
    for index, expense in enumerate(expenses, start=1):
        print(
            f'{index:<5} {expense["date"]:<12} {expense["category"]:<18} '
            f'{expense["amount"]:>10.2f}  {expense["note"]}'
        )


def show_summary(expenses):
    """Display total expenses and totals by category."""
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(expense["amount"] for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\n--- Spending Summary ---")
    print(f"Total expenses: {total:.2f}")
    print("Spending by category:")
    for category, amount in sorted(category_totals.items()):
        print(f"  {category}: {amount:.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View spending summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
