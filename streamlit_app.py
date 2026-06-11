import streamlit as st
import requests

st.set_page_config(page_title="Purchase Prediction")

st.title("🛒 Social Network Ads Prediction")

age = st.number_input(
    "Enter Age",
    min_value=18,
    max_value=100,
    value=35
)

salary = st.number_input(
    "Enter Estimated Salary",
    min_value=0,
    value=50000
)

if st.button("Predict"):

    data = {
        "input": [age, salary]
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=data
        )

        result = response.json()

        prediction = result["prediction"]

        if prediction == 1:
            st.success("✅ User is likely to purchase")
        else:
            st.error("❌ User is unlikely to purchase")

    except Exception as e:
        st.error(f"Error: {e}")