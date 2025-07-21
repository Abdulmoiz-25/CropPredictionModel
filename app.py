import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Load your model
model = pickle.load(open('crop_model.pkl', 'rb'))  # updated filename

# Page configuration
st.set_page_config(page_title="🌾 Crop Prediction App", layout="centered")

# Add custom background image from local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = img_file.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string.decode('latin1')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("background.jpg")

# Custom styles (text shadow, color matching)
st.markdown("""
    <style>
    h1, h2, h3, .stMarkdown, .stButton>button, .stNumberInput label {
        color: #f7f7f7 !important;
        text-shadow: 1px 1px 2px #000000;
    }

    .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 8px;
        color: #000000;
    }

    .stButton>button {
        background-color: #228B22;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1.2rem;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #1e7b1e;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# App UI
st.title("🌾 Crop Prediction App")
st.markdown("### Predict the most suitable crop based on soil and weather conditions.")

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
