import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# Custom CSS to match your video layout
st.markdown("""
    <style>
    .main {
        background: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        color: #2e7d32;
        margin-bottom: 20px;
    }
    .form-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 15px;
        width: 400px;
        margin: auto;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    input[type="number"] {
        border-radius: 8px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Centered title
st.markdown("<div class='title'>Crop Prediction</div>", unsafe_allow_html=True)

# Input form centered in a card
with st.form("crop_form"):
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)

    N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0, format="%.2f")
    P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0, format="%.2f")
    K = st.number_input("Potassium (K)", min_value=0.0, step=1.0, format="%.2f")
    temperature = st.number_input("Temperature (°C)", format="%.2f")
    humidity = st.number_input("Humidity (%)", format="%.2f")
    ph = st.number_input("pH Level", format="%.2f")
    rainfall = st.number_input("Rainfall (mm)", format="%.2f")

    submit = st.form_submit_button("Predict")

    st.markdown("</div>", unsafe_allow_html=True)

# Predict and show result
if submit:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")
