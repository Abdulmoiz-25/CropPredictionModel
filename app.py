import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("crop_model.pkl")

# Set page configuration
st.set_page_config(page_title="Crop Recommendation App", layout="centered")

# Custom background with blur
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("background.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .blurred-box {
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }

    .content-box {
        padding: 2rem;
        border-radius: 15px;
        max-width: 800px;
        margin: 0 auto 1rem auto;
        background-color: rgba(255, 255, 255, 1); /* Full opacity for visibility */
        z-index: 1;
        position: relative;
    }

    .content-box h1, .content-box h2, .content-box h3, .content-box p, .content-box div, .content-box label {
        text-align: center !important;
        color: black !important;
    }

    input[type="number"], .stNumberInput input {
        color: black !important;
    }

    .block-container {
        padding-top: 0rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI inside the blurred box
st.markdown('<div class="blurred-box"><div class="content-box">', unsafe_allow_html=True)

# Title
st.title("🌾 Crop Recommendation System")

# Input features
st.write("Enter the details below to get a crop recommendation:")

N = st.number_input("Nitrogen", min_value=0, max_value=140, value=70)
P = st.number_input("Phosphorous", min_value=5, max_value=145, value=40)
K = st.number_input("Potassium", min_value=5, max_value=205, value=40)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=70.0)
ph = st.number_input("pH", min_value=3.5, max_value=10.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0, value=100.0)

# Predict button
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0].capitalize()}**")

st.markdown('</div></div>', unsafe_allow_html=True)
