import streamlit as st

# Title and description
st.title("Loan Eligibility Calculator")
st.write("Adjust the sliders to check your loan eligibility and your EMI.")

# Sliders for user inputs
income = st.slider("Monthly Income (in Rs)", 1000, 1000000, 500000)
loan_amount = st.slider("Desired Loan Amount (in Rs)", 50000, 1000000, 500000)
loan_tenure = st.slider("Loan Tenure (in years)", 1, 30, 10)
interest_rate = 0.05 

# Eligibility criteria
min_income = 3000

# Check eligibility
if income >= min_income and loan_amount <= (income * 20):
    st.write("**You are eligible for the loan!**")

    # EMI Calculation
    monthly_rate = 0.00416
    n = loan_tenure * 12 
    emi = loan_amount * monthly_rate * (1 + monthly_rate)**n / ((1 + monthly_rate)**n - 1)
    
    st.write(f"Estimated EMI: Rs {emi:.2f} per month")
else:
    st.write("**You are not eligible for the loan based on the current criteria.**")
    