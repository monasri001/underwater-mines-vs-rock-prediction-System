import streamlit as st
import numpy as np
import pickle

# Title
st.title("🔍 Rock vs Mine Prediction")
st.write("Enter 60 sonar signal features to predict if the object is a Rock or a Mine.")

# Load the saved model
@st.cache_resource
def load_model():
    with open("sonar_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# User input
input_text = st.text_area(
    "🔢 Enter 60 comma-separated values (e.g., 0.02, 0.03, ..., 0.04):", height=100
)

if st.button("Predict"):
    try:
        input_values = [float(x.strip()) for x in input_text.split(",")]
        if len(input_values) != 60:
            st.error("❌ You must enter exactly 60 numeric values.")
        else:
            input_array = np.array(input_values).reshape(1, -1)
            prediction = model.predict(input_array)[0]
            label = "Mine" if prediction == 1 else "Rock"
            st.success(f"🎯 Prediction: The object is a **{label}**.")
    except ValueError:
        st.error("❌ Please make sure all values are valid numbers separated by commas.")
