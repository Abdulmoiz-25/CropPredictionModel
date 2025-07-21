import streamlit as st
import base64
import numpy as np
import pandas as pd
import pickle

# Load your model
model = pickle.load(open('crop_model.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Add background with blur effect
def add_blur_background():
    st.markdown(f"""
        <style>
        .stApp {{
            position: relative;
        }}
        .blurred-bg {{
            background-image: url("background.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            filter: blur(8px);
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            z-index: -1;
        }}
        </style>
        <div class="blurred-bg"></div>
    """, unsafe_allow_html=True)

# Inject blurred background
add_blur_background()

# Inject custom styling
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
        color: white !important;
    }

    button[kind="primary"] {
        color: white !important;
    }

    .block-container {
        padding-top: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Start content
st.markdown('<div class="content-box">', unsafe_allow_html=True)

st.title("🌾 Crop Prediction App")
st.markdown("Predict the most suitable crop based on soil and weather conditions.")

st.subheader("📋 Enter the following parameters:")

N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

if st.button("🌿 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

st.markdown('</div>', unsafe_allow_html=True)
