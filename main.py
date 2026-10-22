"""TrackFlow - a simple command-line expense tracker.

Uses only lists, dictionaries, loops, conditionals and functions.
Expenses are kept in memory, so they disappear when the program exits.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CATEGORIES = ["Food", "Transport", "Bills", "Other"]
MAX_AMOUNT = Decimal("1000000000")
CENT = Decimal("0.01")


def get_amount() -> Decimal:
    """Keep asking until the user types a valid positive amount."""
    while True:
        text = input("Enter amount: ").strip()
        try:
            amount = Decimal(text)
        except InvalidOperation:
            print("Please enter a valid number.")
            continue
        if not amount.is_finite():
            print("Please enter a valid number.")
            continue
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        if amount > MAX_AMOUNT:
            print("Amount is too large.")
            continue
        # ROUND_HALF_UP is what people expect from money; the default
        # (ROUND_HALF_EVEN) would turn 12.345 into 12.34.
        return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def get_category() -> str:
    """Show the category list and return the one the user picks."""
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"  {number}. {category}")
    while True:
        choice = input(f"Choose category (1-{len(CATEGORIES)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice. Try again.")


def add_expense(expenses: list[dict]) -> None:
    amount = get_amount()
    category = get_category()
    description = input("Enter description: ").strip() or "(no description)"
    expenses.append(
        {"amount": amount, "category": category, "description": description}
    )
    print("[OK] Expense added successfully!")


def view_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} | "
            f"{expense['amount']:.2f} | {expense['description']}"
        )


def total_spending(expenses: list[dict]) -> None:
    total = sum((expense["amount"] for expense in expenses), Decimal("0"))
    print(f"\nTotal spending: {total:.2f}")


def category_summary(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals: dict[str, Decimal] = {}  # example: {"Food": Decimal("150.00")}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, Decimal("0")) + expense["amount"]
    print("\nSpending by category:")
    for category, amount in totals.items():
        print(f"  {category}: {amount:.2f}")


def main() -> None:
    expenses: list[dict] = []  # a list of dictionaries, one per expense
    print("Welcome to the Expense Tracker!")

    while True:
        print("\n==============================")
        print("EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_spending(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
