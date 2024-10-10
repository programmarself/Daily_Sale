import streamlit as st

# Initialize session state for inputs
if 'salaries' not in st.session_state:
    st.session_state.salaries = [0] * 20  # Adjust the number of employees as needed
if 'daily_expenses' not in st.session_state:
    st.session_state.daily_expenses = [0] * 10  # Adjust the number of daily expense items
if 'service_charges' not in st.session_state:
    st.session_state.service_charges = [0] * 5  # Adjust the number of service charges
if 'utility_bills' not in st.session_state:
    st.session_state.utility_bills = {'beef': 20000, 'chawal': 20000, 'tax': 0, 'salary': 0, 'expenses': 0}

# App Title
st.title("Financial Summary")

# Date
st.write("### Date: 11-10-24")

# Salary Expenses Section
st.subheader("Salary Expenses (EXP#1)")
for i in range(len(st.session_state.salaries)):
    st.session_state.salaries[i] = st.number_input(f"Salary of Employee {i + 1}", 
                                                     value=st.session_state.salaries[i],
                                                     min_value=0, step=100)

# Daily Expenses Section
st.subheader("Daily Expenses (EXP#2)")
daily_expenses_labels = ["Beef", "Total Expense", "Atta Chawal", "Tax", "Milk", "Drinks", "Fish", "NZR Exp", "S.D Exp", "Far Exp"]
for i, label in enumerate(daily_expenses_labels):
    st.session_state.daily_expenses[i] = st.number_input(label, 
                                                           value=st.session_state.daily_expenses[i],
                                                           min_value=0, step=10)

# Service Charges Section
st.subheader("Service Charges")
service_charge_names = ["Nashta", "Ibrahim", "Noor Hayat", "Saeed", "Ismail"]
for i, name in enumerate(service_charge_names):
    st.session_state.service_charges[i] = st.number_input(f"{name} Salary", 
                                                            value=st.session_state.service_charges[i],
                                                            min_value=0, step=100)

# Utility Bills Section
st.subheader("Utility Bills")
utility_bills_labels = ["Beef", "Chawal", "Tax", "Salary", "Expenses"]
for label in utility_bills_labels:
    st.session_state.utility_bills[label.lower()] = st.number_input(label, 
                                                                      value=st.session_state.utility_bills[label.lower()],
                                                                      min_value=0, step=100)

# Calculate totals
total_salary = sum(st.session_state.salaries)
total_daily_expenses = sum(st.session_state.daily_expenses)
total_service_charges = sum(st.session_state.service_charges)
total_utility_bills = sum(st.session_state.utility_bills.values())
total_expenses = total_daily_expenses + total_salary + total_utility_bills
total_sales = 0  # Input your total sales amount here or make it a user input
profit_or_loss = total_sales - total_expenses

# Display calculated results
st.write("### Summary of Financials")
st.write(f"**Total Salary:** {total_salary}")
st.write(f"**Total Daily Expenses:** {total_daily_expenses}")
st.write(f"**Total Service Charges:** {total_service_charges}")
st.write(f"**Total Utility Bills:** {total_utility_bills}")
st.write(f"**Net Expenses:** {total_expenses}")
st.write(f"**Profit/Loss:** {profit_or_loss}")

# Footer or additional notes
st.write("**Note:** Profit/Loss is calculated based on total sales minus total expenses.")
