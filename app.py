import streamlit as st
import base64
import numpy as np
import pandas as pd
import pickle

# Load model
model = pickle.load(open('crop_model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Add blurred background image
def add_blurred_bg(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
        }}
        .bg-blur {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            filter: blur(8px);
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
        }}
        </style>
        <div class="bg-blur"></div>
        """,
        unsafe_allow_html=True
    )

add_blurred_bg("background.jpg")

# Additional styling
st.markdown("""
    <style>
    .content-box {
        padding: 2rem;
        border-radius: 15px;
        max-width: 800px;
        margin: 2rem auto 1rem auto;
        background-color: rgba(255, 255, 255, 0.85);
    }

    @media (max-width: 768px) {
        .content-box {
            padding: 1.2rem;
            margin: 1rem;
        }
    }

    .content-box h1, .content-box h2, .content-box h3, .content-box p, .content-box div {
        text-align: center !important;
        color: black !important;
    }

    input[type="number"] {
        color: black !important;
    }

    button[kind="primary"] {
        color: white !important;
    }

    .block-container {
        padding-top: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Start content box
st.markdown('<div class="content-box">', unsafe_allow_html=True)

# App title
st.title("🌾 Crop Prediction App")
st.markdown("Predict the most suitable crop based on soil and weather conditions.")

# Input
st.subheader("📋 Enter the following parameters:")

N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Prediction
if st.button("🌿 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

# End content box
st.markdown('</div>', unsafe_allow_html=True)
