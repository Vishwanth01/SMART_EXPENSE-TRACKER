import json
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

# ------ LOAD DATA -------
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# ----- SAVE DATA -------
def save_data(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

# ------ ADD EXPENSE -----
def add_expense(expenses):
    # ---- date validation ----
    while True:
        date = input("please enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format, Try again.")

    # category
    categories = ['Food', 'Travel', 'Shopping', 'Bills', 'Rent', 'Others']
    while True:
        category = input(f"Enter category {categories}: ")
        if category in categories:
            break
        else:
            print("Invalid category from the list")

    # amount
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                break
            else:
                print("The amount should be greater than 0")
        except ValueError:
            print("Invalid, enter a valid amount")

    # description
    description = input("Enter the description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description,
    }

    expenses.append(expense)
    save_data(expenses)
    print("Expense saved Successfully!")

# -------- VIEW EXPENSES --------
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No data found")
        return

    for i, exp in enumerate(expenses, start=1):
        print("\nExpense", i)
        print("Date:", exp["date"])
        print("Category:", exp["category"])
        print("Amount:", exp["amount"])
        print("Description:", exp["description"])

# -------- MONTHLY SUMMARY --------
def monthly_summary(expenses):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    filtered = []

    for exp in expenses:
        d = datetime.strptime(exp["date"], "%Y-%m-%d")
        if d.strftime("%m") == month and d.strftime("%Y") == year:
            filtered.append(exp)

    if len(filtered) == 0:
        print("No data for this month")
        return None

    total = sum(exp["amount"] for exp in filtered)

    print("Total Expense:", total)
    print("Number of transactions:", len(filtered))

    return filtered

# -------- CATEGORY BREAKDOWN --------
def category_breakdown(data):
    totals = {}

    for exp in data:
        cat = exp["category"]
        totals[cat] = totals.get(cat, 0) + exp["amount"]

    print("\nCategory wise spending:")
    for key in totals:
        print(key, ":", totals[key])

    return totals

# -------- PIE CHART --------
def show_chart(expenses):
    data = monthly_summary(expenses)
    if data is None:
        return

    totals = category_breakdown(data)

    labels = list(totals.keys())
    values = list(totals.values())

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Chart")
    plt.show()

# -------- INSIGHTS --------
def show_insights(expenses):
    data = monthly_summary(expenses)
    if data is None:
        return

    totals = category_breakdown(data)

    max_cat = max(totals, key=totals.get)
    max_val = totals[max_cat]

    print("Highest spending category:", max_cat)

    total = sum(totals.values())

    if max_val > 0.4 * total:
        print("Warning: High spending on", max_cat)

# -------- CLEAR ALL DATA --------
def clear_data():
    confirm = input("Are you sure you want to delete all expenses? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            json.dump([], file)
        print("All expense data cleared successfully!")
        return []
    else:
        print("Operation cancelled.")
        return None

# -------- MAIN MENU --------
def main_menu():
    expenses = load_data()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Show Chart")
        print("5. Insights")
        print("6. Clear All Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            monthly_summary(expenses)
        elif choice == "4":
            show_chart(expenses)
        elif choice == "5":
            show_insights(expenses)
        elif choice == "6":
            result = clear_data()
            if result is not None:
                expenses = result
        elif choice == "7":
            save_data(expenses)
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# -------- RUN --------
main_menu()
