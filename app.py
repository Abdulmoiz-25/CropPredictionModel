import streamlit as st
import base64
import numpy as np
import pandas as pd
import pickle

# Load model
model = pickle.load(open('crop_model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Add blurred background image using inline CSS with correct z-index
def add_blurred_bg(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: none;
        }}
        .bg-blur {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            filter: blur(8px);
            z-index: -1;
        }}
        </style>
        <div class="bg-blur"></div>
        """,
        unsafe_allow_html=True
    )

# Call function to display background
add_blurred_bg("background.jpg")

# Additional styling for content visibility
st.markdown("""
    <style>
.content-box {
    padding: 2rem;
    border-radius: 15px;
    max-width: 800px;
    margin: 2rem auto 1rem auto;
    z-index: 1;
    position: relative;
}
h1, h2, h3, p, div, label {
    text-align: right !important;
    color: #228B22 !important;
    font-weight: bold !important;
}
input[type="number"], .stNumberInput input {
    color: white !important;
    background-color: white !important;
}
.block-container {
    padding-top: 1rem !important;
}
</style>""", unsafe_allow_html=True)

# Start content box and put ALL content inside
#st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Title and description
st.title("🌾 Crop Prediction App")
st.markdown("Predict the most suitable crop based on soil and weather conditions.")

# Inputs
st.subheader("📋 Enter the following parameters:")
N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Prediction button
if st.button("🌿 Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

# End content box
#st.markdown('</div>', unsafe_allow_html=True)
