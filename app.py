import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    /* Light background and center alignment */
    .main {
        background-color: #f5f7fa;
        padding-top: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }

    .centered-card {
        background-color: white;
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        width: 400px;
        margin: 0 auto;
    }

    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-size: 16px;
        padding: 10px 0;
        border-radius: 10px;
        width: 100%;
        font-weight: 600;
    }

    .title {
        text-align: center;
        color: #2e7d32;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }

    /* Hide default Streamlit footer */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<div class='title'>Crop Prediction</div>", unsafe_allow_html=True)

# ---------- Centered Card Form ----------
with st.form("crop_form"):
    st.markdown("<div class='centered-card'>", unsafe_allow_html=True)

    N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0, format="%.2f")
    P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0, format="%.2f")
    K = st.number_input("Potassium (K)", min_value=0.0, step=1.0, format="%.2f")
    temperature = st.number_input("Temperature (°C)", format="%.2f")
    humidity = st.number_input("Humidity (%)", format="%.2f")
    ph = st.number_input("pH Level", format="%.2f")
    rainfall = st.number_input("Rainfall (mm)", format="%.2f")

    submit = st.form_submit_button("Predict")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Prediction Result ----------
if submit:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")
