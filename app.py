import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Crop Recommender", layout="centered")

# 🧑‍🎨 Custom CSS for full fixes
st.markdown("""
    <style>
    html, body, .stApp {
        height: 100%;
        background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .form-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 16px;
        width: 100%;
        max-width: 500px;
        margin: 5% auto;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }

    .title {
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        color: #2E7D32;
        margin-bottom: 1rem;
    }

    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-size: 16px;
        font-weight: 600;
        padding: 0.6em 1.5em;
        border-radius: 8px;
        width: 100%;
        margin-top: 10px;
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 🌿 UI Box
st.markdown('<div class="form-box">', unsafe_allow_html=True)
st.markdown('<div class="title">🌾 Crop Recommendation</div>', unsafe_allow_html=True)

# Number Inputs
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=150.0, value=50.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=150.0, value=50.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=150.0, value=50.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.5)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.5)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0, step=1.0)

# Predict Button
if st.button("🔍 Predict"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")

st.markdown('</div>', unsafe_allow_html=True)
