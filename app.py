import streamlit as st

# Function to add background with blur and dark overlay
def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
        }}

        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: rgba(0, 0, 0, 0.5);  /* dark overlay */
            backdrop-filter: blur(8px);      /* blur effect */
            z-index: -1;
        }}

        .block-container {{
            position: relative;
            z-index: 1;
        }}

        .stButton>button {{
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background styling
add_bg()

# App title and description
st.title("🌾 Crop Recommendation System")
st.markdown("Enter soil and climate details to predict the most suitable crop.")

# Input fields
nitrogen = st.number_input("Nitrogen Level", min_value=0.0)
phosphorus = st.number_input("Phosphorus Level", min_value=0.0)
potassium = st.number_input("Potassium Level", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH Level", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

# Predict button
if st.button("Predict Crop"):
    # Dummy logic — replace with your trained model prediction
    if nitrogen > 100 and rainfall > 100:
        prediction = "Rice"
    else:
        prediction = "Wheat"
    
    st.success(f"✅ Recommended Crop: **{prediction}**")
