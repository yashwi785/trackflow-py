#expense tracker
expenses = [{"name": "Initial Expense", "amount": 0.0}]
print("Welcome to the Expense Tracker!")
while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expenses.append({"name": expense_name, "amount": expense_amount})
        print(f"Expense '{expense_name}' of amount {expense_amount} added.")

    elif choice == '2':
        if len(expenses) == 1:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses[1:], start=1):
                print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")

    elif choice == '3':
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
