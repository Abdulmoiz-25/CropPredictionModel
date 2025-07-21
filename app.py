import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("crop_model.pkl", "rb"))

# Set Streamlit page config
st.set_page_config(page_title="Crop Recommendation", layout="centered")

# Apply full-page background with reliable method (overlay via CSS on .stApp)
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1400&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .form-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        max-width: 500px;
        margin: 5% auto;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2e7d32;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-size: 16px;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
    }
    </style>
""", unsafe_allow_html=True)

# Start layout
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🌿 Crop Recommendation System</div>', unsafe_allow_html=True)

# Inputs with +/– controls
N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Predict button
if st.button("🌱 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")

st.markdown('</div>', unsafe_allow_html=True)
