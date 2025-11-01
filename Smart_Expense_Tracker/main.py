# Smart Expense Tracker – AI-based Finance Analyzer
# Developed by Bhagya Gandhi

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- Initialize or load CSV ---
try:
    expenses = pd.read_csv("expenses.csv")
except FileNotFoundError:
    expenses = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])
    expenses.to_csv("expenses.csv", index=False)


# --- Auto Categorization Logic ---
def categorize_expense(desc):
    desc = desc.lower()
    if any(word in desc for word in ["food", "pizza", "burger", "restaurant", "lunch", "snack"]):
        return "Food"
    elif any(word in desc for word in ["bus", "train", "cab", "fuel", "petrol", "ticket"]):
        return "Travel"
    elif any(word in desc for word in ["recharge", "electricity", "bill", "internet", "wifi"]):
        return "Utilities"
    elif any(word in desc for word in ["movie", "game", "music", "netflix", "fun"]):
        return "Entertainment"
    elif any(word in desc for word in ["cloth", "shopping", "tshirt", "cap", "shoe"]):
        return "Shopping"
    else:
        return "Other"


# --- Add Expense ---
def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount (₹): "))
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    if date.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = categorize_expense(desc)
    new_row = {"Date": date, "Description": desc, "Amount": amount, "Category": category}
    global expenses
    expenses = pd.concat([expenses, pd.DataFrame([new_row])], ignore_index=True)
    expenses.to_csv("expenses.csv", index=False)
    print(f"✅ Added: {desc} | ₹{amount} | Category: {category}")


# --- View Summary ---
def view_summary():
    print("\n📊 Expense Summary:")
    total = expenses["Amount"].sum()
    by_cat = expenses.groupby("Category")["Amount"].sum()
    print(by_cat)
    print(f"\n💰 Total Spent: ₹{total}")

    # Pie Chart
    if not by_cat.empty:
        by_cat.plot(kind="pie", autopct="%1.1f%%", figsize=(5, 5))
        plt.title("Spending by Category")
        plt.ylabel("")
        plt.show()


# --- Menu ---
def main():
    while True:
        print("\n===== Smart Expense Tracker =====")
        print("1. Add New Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Exiting... Have a good financial day!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
