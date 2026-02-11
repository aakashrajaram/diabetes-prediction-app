import streamlit as st
import numpy as np

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Modern UI CSS
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
}
.card {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.stButton>button {
    background-color: #4facfe;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation", ["Home", "Diabetes Prediction"])

if page == "Home":
    st.markdown('<div class="title">Diabetes Prediction with Machine Learning</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <h3>Welcome 👋</h3>
    <p>This intelligent system predicts diabetes risk based on medical inputs.</p>
    <p>Navigate to <b>Diabetes Prediction</b> from the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Diabetes Prediction":

    st.markdown('<div class="title">Check Your Diabetes Risk</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120, 25)
        glucose = st.number_input("Glucose", 0.0, 300.0, 120.0)
        bp = st.number_input("Blood Pressure", 0.0, 200.0, 70.0)

    with col2:
        insulin = st.number_input("Insulin", 0.0, 900.0, 80.0)
        skin = st.number_input("Skin Thickness", 0.0, 100.0, 20.0)
        bmi = st.number_input("BMI", 0.0, 60.0, 25.0)

    if st.button("Predict Now"):

        # Simple Risk Logic (Lightweight ML-like scoring)
        score = 0
        
        if glucose > 140:
            score += 1
        if bmi > 30:
            score += 1
        if age > 45:
            score += 1
        if bp > 90:
            score += 1

        if score >= 2:
            st.error("⚠ Oops! You have DIABETES")
        else:
            st.success("✅ Great! You DON'T have diabetes")

    st.markdown('</div>', unsafe_allow_html=True)
