import streamlit as st
import pickle
import numpy as np

# Load the saved logistic regression model
model = pickle.load(open('basi.pkl', 'rb'))

# Streamlit app
st.title("Diabetes Prediction")
st.header("Enter the medical details to predict if a person is diabetic")

# Collect user inputs
pregnancies = st.number_input("Number of Pregnancies:", min_value=0, step=1, value=1)
glucose = st.number_input("Glucose Level:", min_value=0, step=1, value=85)
blood_pressure = st.number_input("Blood Pressure (mm Hg):", min_value=0, step=1, value=66)
skin_thickness = st.number_input("Skin Thickness (mm):", min_value=0, step=1, value=29)
insulin = st.number_input("Insulin Level:", min_value=0, step=1, value=0)
bmi = st.number_input("Body Mass Index (BMI):", min_value=0.0, step=0.1, value=26.6)
dpf = st.number_input("Diabetes Pedigree Function (DPF):", min_value=0.0, step=0.001, value=0.351)
age = st.number_input("Age:", min_value=0, step=1, value=31)

# Prepare input data for prediction
if st.button("Predict"):
    try:
        # Combine inputs into a single array
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Display result
        if prediction == 0:
            st.success("The person is NOT diabetic.")
        else:
            st.warning("The person is DIABETIC.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
