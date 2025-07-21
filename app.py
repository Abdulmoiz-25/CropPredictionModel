import streamlit as st
import base64

# Page config
st.set_page_config(page_title="Crop Prediction", layout="centered")

# Add background from local file
def add_bg():
    with open("background.jpg", "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()  # ⬅️ Call the function

# Main title
st.markdown("<h1 style='text-align:center; color:white;'>🌾 Crop Prediction</h1>", unsafe_allow_html=True)

# Form input
with st.form("form"):
    N = st.number_input("Nitrogen", min_value=0)
    P = st.number_input("Phosphorus", min_value=0)
    K = st.number_input("Potassium", min_value=0)
    temp = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")
    submit = st.form_submit_button("Predict")

# Output result
if submit:
    st.success("✅ Predicted Crop: Rice")

# Style the button green
st.markdown("""
    <style>
    .stButton > button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
