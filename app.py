import streamlit as st
import base64

st.set_page_config(page_title="Crop Predictor", layout="centered")

def set_blurred_background(image_file):
    with open(image_file, "rb") as f:
        image_data = f.read()
    encoded = base64.b64encode(image_data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/png;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
        }}

        .blur-container {{
            background-color: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 3rem;
            margin: 5% auto;
            border-radius: 15px;
            max-width: 700px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_blurred_background("background.jpg")

# Place content in blur wrapper
st.markdown("<div class='blur-container'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🌾 Crop Prediction App</h1>", unsafe_allow_html=True)
st.subheader("🔢 Enter Soil and Weather Details")

N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("pH", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

if st.button("Predict"):
    st.success("✅ Based on the input, suitable crop is: **Rice**")

st.markdown("</div>", unsafe_allow_html=True)
