# TrackFlow

A lightweight, interactive command-line expense tracker built in Python. This project was developed to practice and demonstrate the practical application of foundational Python concepts - dynamic loops, nested data structures, and modular function design.

## Core concepts applied

- **Nested dictionaries and lists:** each expense is a dictionary (amount, category, description) held in a list.
- **Control flow and loops:** the menu runs in a `while` loop, with `for` loops for iteration and totals.
- **Input validation:** amounts are parsed with `Decimal` inside a `try/except`, so bad input re-prompts instead of crashing. Money is never stored as a binary float.
- **Functions:** the logic is split into small, reusable blocks.

## Run it

```bash
python main.py
```

No third-party dependencies. Python 3.10+.

## Tests

```bash
python -m unittest discover -s tests -t . -v
```

Tests run on every push and pull request via GitHub Actions.

## Sample terminal output

```text
Welcome to the Expense Tracker!

==============================
EXPENSE TRACKER
==============================
1. Add Expense
2. View All Expenses
3. Total Spending
4. Category Summary
5. Exit

Enter your choice (1-5): 1
Enter amount: 150.00
  1. Food
  2. Transport
  3. Bills
  4. Other
Choose category (1-4): 1
Enter description: Lunch with team
[OK] Expense added successfully!

Enter your choice (1-5): 3

Total spending: 150.00
```

## Project structure

```text
TrackFlow/
|
|-- main.py              # menu loop, validation and reporting
|-- tests/test_main.py   # unit tests for parsing and summaries
`-- README.md
```

## Known limitations

Expenses live in memory only, so they are lost on exit. Persisting them to JSON or SQLite is the next planned step.
