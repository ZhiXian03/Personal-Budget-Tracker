import streamlit as st
import pandas as pd

st.title("Personal Budget Tracker")

# store data
if "data" not in st.session_state:
    st.session_state.data = []

# input
st.subheader("Add a New Expense")
date = st.date_input("Date")
item = st.text_input("Expense Item", expense_options)
amount = st.text_input("Amount (RM)")

expense_options = ["Food", "Transport", "Saving", "Car Loan", "Shopping"]

# button
if st.button("Add Expense"):
    try:
        amount = float(amount)

        if amount < 0:
            st.error("Amount cannot be negative!")
        else:
            st.session_state.data.append({
                "Date": date,
                "Item": item,
                "Amount": amount
            })
            st.success(f"Expense '{item}' added successfully!")

    except:
        st.error("Amount must be a number!")

# display table
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("Expense Summary")
    st.table(df)

    total = df["Amount"].sum()
    st.write(f"Total Expenses: RM {total:.2f}")
