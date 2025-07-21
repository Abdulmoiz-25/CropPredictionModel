import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/4/4e/Crop_fields.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .main-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        max-width: 700px;
        margin: auto;
    }
    .title {
        text-align: center;
        color: #2E7D32;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main app UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🌱 Crop Recommendation System</div>', unsafe_allow_html=True)

st.write("### Please enter soil and environmental values:")

# Input fields with + / - buttons
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0, value=50.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=140.0, value=50.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=50.0, step=1.0)
temperature = st.number_input("Temperature (°C)", value=25.0, step=0.5)
humidity = st.number_input("Humidity (%)", value=60.0, step=1.0)
ph = st.number_input("pH Level", value=6.5, step=0.1)
rainfall = st.number_input("Rainfall (mm)", value=100.0, step=1.0)

# Prediction
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")

st.markdown('</div>', unsafe_allow_html=True)
