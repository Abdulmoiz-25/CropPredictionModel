import streamlit as st
import base64

# Page config
st.set_page_config(page_title="Crop Prediction", layout="centered")

# Set background image with blur effect
def set_bg_blur(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            position: relative;
        }}
        .blur-wrapper {{
            backdrop-filter: blur(8px);
            background-color: rgba(255, 255, 255, 0.2);  /* subtle overlay for better contrast */
            padding: 3rem;
            border-radius: 20px;
            max-width: 700px;
            margin: auto;
            margin-top: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply blur background
set_bg_blur("background.jpg")

# App content inside blur wrapper
st.markdown("<div class='blur-wrapper'>", unsafe_allow_html=True)

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
