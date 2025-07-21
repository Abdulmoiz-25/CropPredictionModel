import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Crop Prediction App", layout="centered")

# Function to add styled background image
def add_bg():
    with open("background.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            background: none;
        }}

        .stApp::before {{
            content: "";
            background: url("data:image/jpg;base64,{encoded_string}") no-repeat center center fixed;
            background-size: cover;
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            z-index: -2;
            filter: blur(6px) brightness(0.4); /* Blur and dim */
        }}

        .main-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem auto;
            max-width: 700px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        }}

        h1, .stTextInput label, .stNumberInput label, .stSelectbox label, .stSubheader, .stMarkdown {{
            color: #1a1a1a;
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
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# Start of App Layout
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

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

    st.markdown('</div>', unsafe_allow_html=True)
