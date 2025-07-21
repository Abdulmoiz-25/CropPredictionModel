import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# Set page config
st.set_page_config(page_title="Crop Recommendation", layout="centered")

# Inject custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    h1 {
        text-align: center;
        color: #2E7D32;
    }
    .css-1aumxhk {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Content
st.markdown("<h1>🌿 Crop Recommendation System</h1>", unsafe_allow_html=True)
with st.container():
    with st.form("crop_form"):
        st.markdown('<div class="main-card">', unsafe_allow_html=True)

        N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
        K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=6.5)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

        submitted = st.form_submit_button("🔍 Predict Crop")

        st.markdown("</div>", unsafe_allow_html=True)

        if submitted:
            input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            prediction = model.predict(input_data)[0]
            st.success(f"✅ Recommended Crop: **{prediction}**")
