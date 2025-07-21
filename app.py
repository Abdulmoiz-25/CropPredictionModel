import streamlit as st

# Set page config
st.set_page_config(page_title="Crop Prediction", layout="centered")

# Apply custom CSS for background and form styling
st.markdown("""
    <style>
        /* Fullscreen background image */
        body {
            background-image: url('https://i.ibb.co/hyCHDk1/plant-bg.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Hide Streamlit default menu and footer */
        #MainMenu, footer, header {visibility: hidden;}

        /* Center form container */
        .form-container {
            background: rgba(255, 255, 255, 0.8);
            padding: 2rem;
            border-radius: 20px;
            max-width: 400px;
            margin: 8% auto;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }

        .form-container h2 {
            text-align: center;
            color: #2E7D32;
            font-size: 28px;
            margin-bottom: 20px;
        }

        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 20px;
            padding: 0.5em 2em;
            border: none;
        }

        .stButton > button:hover {
            background-color: #388E3C;
        }
    </style>
""", unsafe_allow_html=True)

# Use HTML block for form styling
st.markdown('<div class="form-container"><h2>Crop Prediction</h2>', unsafe_allow_html=True)

# Input fields
nitrogen = st.text_input("Nitrogen (N)")
phosphorus = st.text_input("Phosphorus (P)")
potassium = st.text_input("Potassium (K)")
temperature = st.text_input("Temperature (°C)")
humidity = st.text_input("Humidity (%)")
ph = st.text_input("pH Level")
rainfall = st.text_input("Rainfall (mm)")

# Predict button
if st.button("Predict"):
    st.success("✅ Your predicted crop is: Wheat 🌾")

# End HTML block
st.markdown('</div>', unsafe_allow_html=True)
