import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Crop Prediction App", layout="centered")

# Function to add background image
def add_bg():
    with open("background.jpg", "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                padding: 2rem;
            }}

            .stButton > button {{
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
            }}

            .stButton > button:hover {{
                background-color: #27ae60;
                color: white;
            }}

            .stNumberInput input {{
                background-color: white;
                color: black;
                border-radius: 5px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

add_bg()

# App title
st.markdown("<h1 style='text-align: center; color: white;'>🌾 Crop Prediction App</h1>", unsafe_allow_html=True)

# Input fields
st.subheader("🔢 Enter Soil and Weather Details")

N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
ph = st.number_input("pH", min_value=0.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    st.success("✅ Based on the input, suitable crop is: **Rice**")  # Replace with your model’s prediction

