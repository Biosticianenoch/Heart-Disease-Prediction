#!/usr/bin/env python
# coding: utf-8
import pickle
import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# ---------------- VISITOR COUNTER ----------------
counter_file = "visitor_data.pkl"

# Load or initialize visitor data
if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {
        'count': 0,
        'timestamps': []  # List to store datetime strings
    }

# Update visitor count (only once per session)
if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

# ---------------- LOAD MODEL ----------------
MODEL_DIR = os.path.expanduser("~/Downloads")  # Adjust path as needed
MODEL_PATH = os.path.join(MODEL_DIR, "heart_disease_model1.sav")

@st.cache_resource
def load_model(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

heart_model = load_model(MODEL_PATH)

# ---------------- SIDEBAR MENU ----------------
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["Welcome", "Prediction", "Recommendation", "FAQ", "Disclaimer", "Analytics"], 
                           icons=['house', 'activity', 'heart', 'question-circle', 'exclamation-circle', 'bar-chart'],
                           menu_icon="cast", default_index=0)

# ---------------- WELCOME PAGE ----------------
if selected == "Welcome":
    st.markdown("<h1 style='text-align: center; color: crimson;'>💓 Welcome to Heart Disease Risk Estimator</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", use_column_width=True)
    
    st.success(f"🌟 **Total Visitors:** {visitor_data['count']}")

    st.write("""
    **This app predicts your risk for heart disease based on health parameters.**

    ✅ Easy to use  
    ✅ Quick prediction  
    ✅ Personalized recommendations  

    👉 Use the sidebar to get started!
    """)

# ---------------- PREDICTION PAGE ----------------
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center;'>🩺 Heart Disease Prediction</h2>", unsafe_allow_html=True)
    st.write("Fill in the following details:")

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", min_value=1, help="Age in years")
            trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, help="Normal ~120 mm Hg")
            restecg = st.selectbox(
                "Resting ECG Results", 
                [0, 1, 2], 
                format_func=lambda x: {0: "Normal", 1: "Having ST-T wave abnormality", 2: "Showing probable/definite left ventricular hypertrophy"}[x],
                help="Electrocardiographic results"
            )
            oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, format="%.1f")

        with col2:
            sex = st.selectbox(
                "Sex", 
                [1, 0], 
                format_func=lambda x: "Male" if x == 1 else "Female",
                help="Gender of the person"
            )
            chol = st.number_input("Cholesterol (mg/dl)", min_value=100, help="Desirable < 200 mg/dl")
            thalach = st.number_input("Max Heart Rate Achieved", min_value=60, help="Typically 100–200")
            slope = st.selectbox(
                "ST Slope", 
                [0, 1, 2], 
                format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x],
                help="Slope of the peak exercise ST segment"
            )

        with col3:
            cp = st.selectbox(
                "Chest Pain Type", 
                [0, 1, 2, 3], 
                format_func=lambda x: {0: "Typical Angina", 1: "Atypical Angina", 2: "Non-anginal Pain", 3: "Asymptomatic"}[x],
                help="Type of chest pain experienced"
            )
            fbs = st.selectbox(
                "Fasting Blood Sugar > 120 mg/dl", 
                [1, 0], 
                format_func=lambda x: "Yes (>120 mg/dl)" if x == 1 else "No (<=120 mg/dl)",
                help="Is fasting blood sugar > 120 mg/dl?"
            )
            exang = st.selectbox(
                "Exercise Induced Angina", 
                [1, 0], 
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Exercise-induced angina presence"
            )
            ca = st.selectbox(
                "Number of Major Vessels Colored by Fluoroscopy (0–4)", 
                [0, 1, 2, 3, 4],
                help="Number of major vessels colored by fluoroscopy"
            )
            thal = st.selectbox(
                "Thalassemia", 
                [1, 2, 3], 
                format_func=lambda x: {1: "Normal", 2: "Fixed Defect", 3: "Reversible Defect"}[x],
                help="Thalassemia type"
            )

        submitted = st.form_submit_button("Predict Heart Disease")

    if submitted:
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]

        input_array = np.array(input_data).reshape(1, -1)
        prediction = heart_model.predict(input_array)[0]
        probability = heart_model.predict_proba(input_array)[0][1] * 100

        if prediction == 1:
            st.error(f"🚨 The person is **likely** to have heart disease.\n\n🧠 Prediction Confidence: {probability:.2f}%")
        else:
            st.success(f"✅ The person is **unlikely** to have heart disease.\n\n🧠 Prediction Confidence: {probability:.2f}%")

# ---------------- RECOMMENDATION PAGE ----------------
elif selected == "Recommendation":
    st.markdown("<h2 style='text-align: center;'>💡 Health Recommendations</h2>", unsafe_allow_html=True)
    st.write("""
    Based on your prediction result, here are some general recommendations:
    
    - 🥗 **Healthy Diet:** Adopt a low-fat, high-fiber diet with plenty of fruits and vegetables.
    - 🏃 **Exercise Regularly:** At least 30 minutes of moderate activity most days.
    - 🚭 **Avoid Smoking:** Quit smoking to improve heart and lung health.
    - 🍷 **Limit Alcohol:** Keep alcohol consumption moderate.
    - 💊 **Medication:** Follow medical advice and take prescribed medications.
    - 🧘 **Stress Management:** Practice mindfulness, yoga or meditation.
    
    **Note:** Always consult with a healthcare provider for personalized recommendations.
    """)

# ---------------- FAQ PAGE ----------------
elif selected == "FAQ":
    st.markdown("<h2 style='text-align: center;'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)
    st.write("""
    **Q1:** What is this app for?  
    👉 This app predicts the likelihood of heart disease based on medical parameters.

    **Q2:** Is this a replacement for medical diagnosis?  
    👉 **No.** This app is for **screening purposes only**. Always consult a certified doctor.

    **Q3:** What data is used for prediction?  
    👉 Based on the **UCI Heart Disease dataset** and trained via supervised machine learning.

    **Q4:** Is my data stored?  
    👉 No personal health data is stored — predictions are made locally on your device.
    """)

# ---------------- DISCLAIMER PAGE ----------------
elif selected == "Disclaimer":
    st.markdown("<h2 style='text-align: center;'>⚠️ Disclaimer</h2>", unsafe_allow_html=True)
    st.warning("""
    - This app is **strictly for screening purposes** only.
    - It does **not provide medical advice** or diagnosis.
    - Please consult with a licensed healthcare provider for any health concerns.
    - The developers are not responsible for any health decisions based on this app.
    """)

# ---------------- ANALYTICS PAGE ----------------
elif selected == "Analytics":
    st.markdown("<h2 style='text-align: center;'>📊 Visitor Analytics</h2>", unsafe_allow_html=True)

    st.info(f"🧑‍💻 **Total Visitors:** {visitor_data['count']}")

    if len(visitor_data['timestamps']) > 0:
        st.write("### 🕒 **Visitor Log (Timestamps):**")
        st.dataframe(visitor_data['timestamps'])

    # Option to reset the counter
    if st.button("🔄 Reset Visitor Counter"):
        visitor_data = {'count': 0, 'timestamps': []}
        with open(counter_file, 'wb') as f:
            pickle.dump(visitor_data, f)
        st.success("Visitor counter has been reset. Please refresh to see the update.")

    st.write("⚠️ **Note:** This data is stored locally in `visitor_data.pkl`. No external tracking is used.")
