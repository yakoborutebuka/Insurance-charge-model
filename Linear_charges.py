import streamlit as st
import numpy as np
import joblib

# Load the trained Linear Regression model
model = joblib.load('/content/linear_regression_model.joblib')

claim_amount = st.number_input("Claim Amount", min_value=0.0, format="%.2f")
past_consultations = st.number_input("Number of Past Consultations", min_value=0)
hospital_expenditure = st.number_input("Hospital Expenditure", min_value=0.0, format="%.2f")
annual_salary = st.number_input("Annual Salary", min_value=0.0,format="%.2f")
children = st.number_input("Number of Children", min_value=0,max_value=5)
smoker = st.selectbox("Is the person a smoker?", ["No", "Yes"])

# Encode smoker (0 = No, 1 = Yes)
smoker_encoded = 1 if smoker == "Yes" else 0

# Predict button
if st.button("Predict Insurance Charges"):
    # Create input array
    input_data = np.array([[claim_amount, past_consultations, hospital_expenditure, annual_salary, children, smoker_encoded]]) # predict for 1 person, 6 features

    # Make prediction
   # prediction = model.predict(input_data)[0]
    prediction1=model.predict(input_data)[0]

    #st.success(f"💰 Estimated Insurance Charges: ₹{prediction:,.2f}")
    st.success(f"💰 Estimated Insurance Charges: ₹{prediction1:,.2f}")
