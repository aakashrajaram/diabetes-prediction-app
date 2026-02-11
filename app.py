import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_diabetes

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# ----------------------------
# Custom CSS for Modern UI
# ----------------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #4facfe, #00f2fe);
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    }
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background-color: #4facfe;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Load and Train Model
# ----------------------------
data = load_diabetes()
X = data.data
y = (data.target > data.target.mean()).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train, y_train)

# ----------------------------
# Sidebar Navigation
# ----------------------------
page = st.sidebar.radio("Navigation", ["Home", "Diabetes Prediction"])

# ----------------------------
# Home Page
# ----------------------------
if page == "Home":
    st.markdown('<div class="title">Diabetes Prediction with Machine Learning</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <h3>Welcome 👋</h3>
    <p>This intelligent system predicts whether a person has diabetes 
    based on medical inputs using Machine Learning.</p>
    <p>👉 Navigate to <b>Diabetes Prediction</b> from the sidebar to begin.</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Prediction Page
# ----------------------------
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

        input_data = np.array([[age, glucose, bp, insulin, skin, bmi, 0, 0, 0, 0]])
        input_data = scaler.transform(input_data)

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠ Oops! You have DIABETES")
        else:
            st.success("✅ Great! You DON'T have diabetes")

    st.markdown('</div>', unsafe_allow_html=True)
