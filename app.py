import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('house_price_model.pkl')

# Page title
st.title("🏠 House Price Predictor")

st.write("Enter house details below")

# Inputs
area_sqft = st.number_input("Area (sqft)", min_value=100)

bedrooms = st.number_input("Bedrooms", min_value=1)

bathrooms = st.number_input("Bathrooms", min_value=1)

floors = st.number_input("Floors", min_value=1)

age_of_property = st.number_input("Age of Property", min_value=0)

parking_spaces = st.number_input("Parking Spaces", min_value=0)

locality = st.selectbox(
    "Locality",
    ['Palm Residency', 'Green Park', 'Sunrise Colony']
)

house_type = st.selectbox(
    "House Type",
    ['Apartment', 'Independent House', 'Villa']
)

# Predict button
if st.button("Predict Price"):

    user_df = pd.DataFrame({
        'AREA_SQFT': [area_sqft],
        'BEDROOMS': [bedrooms],
        'BATHROOMS': [bathrooms],
        'FLOORS': [floors],
        'AGE_OF_PROPERTY': [age_of_property],
        'PARKING_SPACES': [parking_spaces],
        'LOCALITY': [locality],
        'HOUSE_TYPE': [house_type]
    })

    prediction = model.predict(user_df)

    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")