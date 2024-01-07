import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load model
model = pickle.load(open("Strokepred.ipynb", "rb"))

# Create LabelEncoders for categorical features
smoking_encoder = LabelEncoder()
smoking_encoder.fit(["formerly smoked", "never smoked", "smokes", "Unknown"])
residence_encoder = LabelEncoder()
residence_encoder.fit(["Urban", "Rural"])

# App title and layout
st.set_page_config(page_title="Stroke Prediction App", layout="centered")

# Input features with appropriate types and options
st.header("Enter Patient Information:")

gender = st.radio("Gender", options=["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120)
hypertension = st.selectbox("Hypertension", options=["Yes", "No"])
heart_disease = st.selectbox("Heart Disease", options=["Yes", "No"])
residence_type = st.selectbox("Residence Type", options=["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=100.0)
smoking_status = st.selectbox("Smoking Status", options=["formerly smoked", "never smoked", "smokes", "Unknown"])

# Create a DataFrame with input features
df = pd.DataFrame({
    "gender": [gender],
    "age": [age],
    "hypertension": [1 if hypertension == "Yes" else 0],
    "heart_disease": [1 if heart_disease == "Yes" else 0],
    "Residence_type": residence_encoder.transform([residence_type])[0],
    "avg_glucose_level": [avg_glucose_level],
    "bmi": [bmi],
    "smoking_status": smoking_encoder.transform([smoking_status])[0]
})

# Predict when button is clicked
if st.button("Predict Stroke Risk"):
    prediction = model.predict(df)[0]
    st.header("Predicted Stroke Risk:")
    st.subheader(f"{prediction:.4f}")  # Display prediction with 4 decimal places


