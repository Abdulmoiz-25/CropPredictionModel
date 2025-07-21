import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('crop_model.pkl', 'rb'))

# Set page config
st.set_page_config(layout="wide")

# Set custom CSS for background and content box
def add_bg_and_style():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1500&q=80');
            background-size: cover;
            background-position: center;
            filter: blur(0px);
        }}
        .content-box {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            margin: 2rem auto;
            border-radius: 15px;
            max-width: 700px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        @media (max-width: 768px) {{
            .content-box {{
                padding: 1.5rem;
                margin: 1rem;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function
add_bg_and_style()

# Main UI inside a styled div
st.markdown("<div class='content-box'>", unsafe_allow_html=True)

st.title("🌾 Crop Prediction App")
st.markdown("Enter the following soil and environmental conditions to predict the most suitable crop:")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH value")
rainfall = st.number_input("Rainfall (mm)")

# Prediction
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"🌱 The recommended crop to grow is: **{prediction[0].capitalize()}**")

st.markdown("</div>", unsafe_allow_html=True)
