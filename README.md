# Task 3: Practical Implementation Project
## Personal Expense Tracker

A command-line Python application for recording everyday expenses and reviewing spending.

### Features
- Add an expense with category, amount, and optional note.
- Automatically records the current date.
- View all recorded expenses.
- View total spending and totals grouped by category.
- Saves records in `expenses.csv` so they remain available after restarting.
- Validates amount input and handles common file errors.
- Uses only the Python standard library.

### Requirements
- Python 3.8 or later
- No external packages

### Run
```bash
python expense_tracker.py
```

### Menu
1. Add expense
2. View expenses
3. View spending summary
4. Exit

### Files
- `expense_tracker.py`: application source code
- `README.md`: documentation
- `TASK3_REPORT.docx`: internship report
- `TASK3_DESCRIPTION.txt`: description for the internship portal
- `expenses.csv`: created automatically when an expense is saved

### Testing suggestions
1. Add a valid expense such as Food, 150, Lunch.
2. Try entering text or a negative amount for the amount; the program should ask again.
3. View history and summary.
4. Exit and restart; saved expenses should still be available.
