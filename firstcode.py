# Expense Tracker Project 

import json  

# Load expenses from file
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

 # Function to save expenses
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)   

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1️⃣ Add Expense
    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")

            expense = {
                "amount": amount,
                "category": category,
                "date": date
            }

            expenses.append(expense)
            save_expenses()
            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    # 2️⃣ View Expenses
    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. Amount: {exp['amount']}, "
                      f"Category: {exp['category']}, "
                      f"Date: {exp['date']}")

    # 3️⃣ Update Expense
    elif choice == "3":
        if not expenses:
            print("No expenses to update.")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp}")

            try:
                num = int(input("Enter expense number to update: ")) - 1

                if 0 <= num < len(expenses):
                    expenses[num]['amount'] = float(input("New amount: "))
                    expenses[num]['category'] = input("New category: ")
                    expenses[num]['date'] = input("New date: ")
                    print("Expense updated successfully!")
                    save_expenses()
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Please enter a valid number.")

    # 4️⃣ Delete Expense
    elif choice == "4":
        if not expenses:
            print("No expenses to delete.")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp}")

            try:
                num = int(input("Enter expense number to delete: ")) - 1

                if 0 <= num < len(expenses):
                    expenses.pop(num)
                    save_expenses()
                    print("Expense deleted successfully!")
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Invalid input.")

    # 5️⃣ Reports
    elif choice == "5":
        if not expenses:
            print("No expenses to generate report.")
        else:
            total = sum(exp["amount"] for exp in expenses)
            print("\n===== Expense Report =====")
            print(f"Total Expenses: {total}")

            # Category-wise report
            categories = {}
            for exp in expenses:
                categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

            print("\nCategory-wise Breakdown:")
            for cat, amt in categories.items():
                print(f"{cat}: {amt}")

    # 6️⃣ Exit
    elif choice == "6":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")