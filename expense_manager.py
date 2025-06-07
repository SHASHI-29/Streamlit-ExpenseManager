# expense_manager.py

import pandas as pd

# Load or initialize expense DataFrame
def init_expense_data():
    return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Add a new expense
def add_expense(df, date, category, amount, description):
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Description": description}
    return pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)

# Calculate summary
def calculate_summary(df):
    total = df["Amount"].sum()
    by_category = df.groupby("Category")["Amount"].sum().reset_index()
    return total, by_category
