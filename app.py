import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('crop_model.pkl', 'rb'))

# Custom CSS
st.markdown("""
    <style>
        body {
            margin: 0;
        }
        .stApp {
            background-image: url('background.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            filter: blur(0px);
        }
        .blur-box {
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            margin: auto;
            width: 90%;
            max-width: 600px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        h1, h2, h3, p, label, div, .st-bb, .st-bq {
            color: black !important;
        }
        .stButton>button {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Start of app
with st.container():
    st.markdown('<div class="blur-box">', unsafe_allow_html=True)

    st.title('🌾 Crop Prediction App')
    st.markdown("### Enter the details below:")

    # Input features
    N = st.number_input('Nitrogen')
    P = st.number_input('Phosphorus')
    K = st.number_input('Potassium')
    temperature = st.number_input('Temperature')
    humidity = st.number_input('Humidity')
    ph = st.number_input('pH Level')
    rainfall = st.number_input('Rainfall (mm)')

    # Prediction
    if st.button('Predict'):
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(data)
        st.success(f'🌱 Recommended Crop: **{prediction[0]}**')

    st.markdown('</div>', unsafe_allow_html=True)
