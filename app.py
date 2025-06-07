# app.py

import streamlit as st
from datetime import date
from expense_manager import init_expense_data, add_expense, calculate_summary
from plotter import plot_expense_pie, plot_bar_chart

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = init_expense_data()

st.title("💰 Personal Expense Tracker")

# --- Input section ---
st.header("Add a new expense")

with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        exp_date = st.date_input("Date", value=date.today())
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    with col2:
        amount = st.number_input("Amount", min_value=0.0, step=1.0)
        description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        st.session_state.expenses = add_expense(st.session_state.expenses, exp_date, category, amount, description)
        st.success("Expense added successfully!")

# --- Table section ---
st.header("📋 Expense Table")
st.dataframe(st.session_state.expenses)

# --- Summary section ---
st.header("📊 Summary")
total, by_category = calculate_summary(st.session_state.expenses)
st.write(f"**Total Expenses:** ₹{total:.2f}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Pie Chart")
    st.pyplot(plot_expense_pie(by_category))

with col2:
    st.subheader("Bar Chart")
    if not by_category.empty:
        st.pyplot(plot_bar_chart(by_category))
    else:
        st.write("No data available to plot.")
