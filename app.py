import streamlit as st
import base64
import numpy as np
import pandas as pd
import pickle

# Load your model
model = pickle.load(open('crop_prediction_model.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Function to add a blurred background image
def add_bg():
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2");
            background-size: cover;
            background-position: center;
            backdrop-filter: blur(6px);
        }
        </style>
    """, unsafe_allow_html=True)

add_bg()

# Add styling for the content box
st.markdown("""
    <style>
    .content-box {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.2);
        max-width: 800px;
        margin: 3rem auto;
    }

    @media (max-width: 768px) {
        .content-box {
            padding: 1.2rem;
            margin: 1rem;
        }
    }

    .content-box h1, .content-box h2, .content-box h3, .content-box p, .content-box div {
        text-align: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# Start content box
st.markdown('<div class="content-box">', unsafe_allow_html=True)

# App title and intro
st.title("🌾 Crop Prediction App")
st.markdown("Predict the most suitable crop based on soil and weather conditions.")

# Input fields
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
