import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# create file with headers if it doesn't exist
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass  # file already exists

# add new expense
def add_expense():
    category = input("Enter category (e.g. Food, Travel, Bills): ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("\n✅ Expense added successfully!\n")

# view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            print("\nAll Expenses:\n")
            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]} | {row[3]}")
    except FileNotFoundError:
        print("No expenses found. Please add some first.")

# view total expenses
def total_expenses():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Expenses: ₹{total:.2f}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# main menu
def main():
    initialize_file()
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
