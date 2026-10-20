# TrackFlow - a simple command-line expense tracker
# Uses only: lists, dictionaries, loops, if/else and functions.
# Note: expenses are kept in memory, so they disappear when the program exits.

CATEGORIES = ["Food", "Transport", "Bills", "Other"]


def get_amount():
    """Keep asking until the user types a valid positive number."""
    while True:
        text = input("Enter amount: ")
        # isdigit() works on whole numbers only, so remove one dot first
        if text.replace(".", "", 1).isdigit():
            amount = float(text)
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


def get_category():
    """Show the category list and return the one the user picks."""
    for number in range(len(CATEGORIES)):
        print(f"  {number + 1}. {CATEGORIES[number]}")
    while True:
        choice = input("Choose category (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice. Try again.")


def add_expense(expenses):
    amount = get_amount()
    category = get_category()
    description = input("Enter description: ")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    print("[✓] Expense added successfully!")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print("\nAll expenses:")
    for i in range(len(expenses)):
        e = expenses[i]
        print(f"{i + 1}. {e['category']} | {e['amount']:.2f} | {e['description']}")


def total_spending(expenses):
    total = 0
    for e in expenses:
        total = total + e["amount"]
    print(f"\nTotal spending: {total:.2f}")


def category_summary(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    totals = {}  # example: {"Food": 150.0, "Bills": 1200.0}
    for e in expenses:
        category = e["category"]
        if category in totals:
            totals[category] = totals[category] + e["amount"]
        else:
            totals[category] = e["amount"]
    print("\nSpending by category:")
    for category in totals:
        print(f"  {category}: {totals[category]:.2f}")


def main():
    expenses = []  # a list of dictionaries, one per expense
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

        choice = input("\nEnter your choice (1-5): ")

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


main()
