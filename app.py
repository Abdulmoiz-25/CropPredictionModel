import streamlit as st
import base64
import numpy as np
import pandas as pd
import pickle

# Load your model
model = pickle.load(open('crop_model.pkl', 'rb'))  # corrected filename

# Set page config
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Function to add a local background image via base64
def add_local_bg(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_local_bg("background.jpg")  # ensure this image is in the same folder

# Custom styling (adjusted text color for visibility on dark image)
st.markdown("""
    <style>
    .content-box {
        background-color: rgba(0, 0, 0, 0);  /* Transparent box */
        padding: 2rem;
        border-radius: 15px;
        color: #ffffff;
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
        color: #f0f0f0 !important;
    }

    label, .st-bb, .st-c3 {
        color: #ffffff !important;
    }

    .stNumberInput > div > input {
        background-color: rgba(255,255,255,0.2);
        color: white;
    }

    .stButton > button {
        background-color: #28a745;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }

    .stButton > button:hover {
        background-color: #218838;
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
