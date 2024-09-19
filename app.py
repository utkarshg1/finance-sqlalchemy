import streamlit as st
import plotly.express as px
from database import add_expense, add_income, get_expenses, get_income
import pandas as pd
from datetime import date

# Set app header and title
st.set_page_config(page_title="Expense manager", page_icon="💰")
st.title("Personal Finance Manager")

# Option to add income or expense
st.sidebar.title("Add Transaction")
transaction_type = st.sidebar.selectbox("Transaction Type", ["Income", "Expense"])

# Form to input income or expense details
if transaction_type == "Income":
    with st.sidebar.form("income_form"):
        source = st.text_input("Income Source")
        income_amount = st.number_input("Income Amount", min_value=0.0)
        income_date = st.date_input(
            "Date", value=date.today()
        )  # Add date field with default as today
        submitted = st.form_submit_button("Add Income")

        if submitted:
            # Convert selected date to datetime for consistency with the database
            add_income(source, income_amount, income_date)
            st.sidebar.success("Income added successfully!")

elif transaction_type == "Expense":
    with st.sidebar.form("expense_form"):
        name = st.text_input("Expense Name")
        expense_amount = st.number_input("Expense Amount", min_value=0.0)
        category = st.selectbox(
            "Category", ["Food", "Rent", "Utilities", "Miscellaneous"]
        )
        expense_date = st.date_input(
            "Date", value=date.today()
        )  # Add date field with default as today
        submitted = st.form_submit_button("Add Expense")

        if submitted:
            # Convert selected date to datetime for consistency with the database
            add_expense(name, expense_amount, category, expense_date)
            st.sidebar.success("Expense added successfully!")

# Fetch expenses and income from the database
expenses = get_expenses()
income = get_income()

# Convert the data to pandas DataFrames
expense_data = {
    "Name": [expense.name for expense in expenses],
    "Amount": [expense.amount for expense in expenses],
    "Category": [expense.category for expense in expenses],
    "Date": [expense.date for expense in expenses],
}
income_data = {
    "Source": [inc.source for inc in income],
    "Amount": [inc.amount for inc in income],
    "Date": [inc.date for inc in income],
}

expense_df = pd.DataFrame(expense_data)
income_df = pd.DataFrame(income_data)

# Show tables of expenses and income
if not income_df.empty:
    st.subheader("Income Table")
    st.dataframe(income_df)
else:
    st.info("No income records found.")

if not expense_df.empty:
    st.subheader("Expense Table")
    st.dataframe(expense_df)
else:
    st.info("No expense records found.")

# Calculate and display the balance
if not expense_df.empty and not income_df.empty:
    total_income = income_df["Amount"].sum()
    total_expense = expense_df["Amount"].sum()
    balance = total_income - total_expense

    st.subheader(f"Current Balance: ${balance:.2f}")

    # Plot total income vs total expense
    st.subheader("Income vs Expenses")
    finance_data = {
        "Category": ["Income", "Expenses"],
        "Amount": [total_income, total_expense],
    }
    finance_df = pd.DataFrame(finance_data)
    fig = px.pie(
        finance_df, values="Amount", names="Category", title="Income vs Expenses"
    )
    st.plotly_chart(fig)

    # Show daily expense and income trends
    st.subheader("Daily Income and Expense Trends")
    income_df["Date"] = pd.to_datetime(income_df["Date"]).dt.date
    expense_df["Date"] = pd.to_datetime(expense_df["Date"]).dt.date

    daily_income = income_df.groupby("Date")["Amount"].sum().reset_index()
    daily_expense = expense_df.groupby("Date")["Amount"].sum().reset_index()

    line_chart = px.line(daily_income, x="Date", y="Amount", title="Daily Income")
    st.plotly_chart(line_chart)

    line_chart_expense = px.line(
        daily_expense, x="Date", y="Amount", title="Daily Expenses"
    )
    st.plotly_chart(line_chart_expense)

else:
    st.warning("No transactions recorded yet.")
