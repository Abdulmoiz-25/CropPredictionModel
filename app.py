import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Crop Prediction App", layout="centered")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        /* Background image */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: url("data:image/jpg;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
            filter: blur(8px) brightness(0.3);
            z-index: -1;
        }}

        /* Main content box styling */
        .main .block-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.3);
        }}

        /* Button styling */
        .stButton > button {{
            background-color: #2ecc71;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
        }}

        .stButton > button:hover {{
            background-color: #27ae60;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("background.jpg")

# App content
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
