
# 💓 Heart Disease Prediction Web App

## 📌 Overview
The **Heart Disease Prediction App** is an interactive **Streamlit-based web application** that uses **Machine Learning** to predict the risk of heart disease based on key health parameters.  

It provides:
- ✅ Easy-to-use interface  
- ✅ Real-time predictions  
- ✅ Personalized recommendations  
- ✅ Visitor analytics tracking  

This tool is designed **for screening purposes only** and should not replace professional medical advice.  

---

## 🛠️ Features
### 🔹 1. Welcome Page
- Beautiful landing page with animated visuals.  
- Displays **total number of visitors** (tracked locally).  
- Quick overview of the app and instructions.  

### 🔹 2. Prediction Page
- Collects medical parameters from the user, including:
  - Age  
  - Gender (Sex)  
  - Chest Pain Type  
  - Resting Blood Pressure  
  - Serum Cholesterol  
  - Fasting Blood Sugar  
  - Resting ECG Results  
  - Maximum Heart Rate Achieved  
  - Exercise-Induced Angina  
  - ST Depression (Oldpeak)  
  - ST Slope  
  - Number of Major Vessels (Ca)  
  - Thalassemia  

- Runs predictions using a **pre-trained ML model (`heart_disease_model1.sav`)**.  
- Displays:
  - **Prediction Result**: Likely/Unlikely to have heart disease.  
  - **Confidence Score** (probability %).  

### 🔹 3. Recommendation Page
Provides **general health recommendations**, such as:
- 🥗 Healthy diet  
- 🏃 Regular exercise  
- 🚭 Avoid smoking  
- 🍷 Limit alcohol intake  
- 💊 Medication adherence  
- 🧘 Stress management techniques  

### 🔹 4. FAQ Page
Answers common questions:
- Purpose of the app  
- Dataset & ML model used  
- Clarification that this is **not a diagnosis tool**  
- Data privacy assurance  

### 🔹 5. Disclaimer Page
- Clearly states the **screening-only** purpose of the app.  
- No medical advice or professional diagnosis.  
- Encourages consultation with healthcare providers.  

### 🔹 6. Analytics Page
- Tracks **visitor count** and **timestamps**.  
- Stores visitor data in a local file: `visitor_data.pkl`.  
- Option to **reset the visitor counter**.  
- No external tracking is used (100% privacy).  

---

## 🧑‍💻 Tech Stack
- **Frontend & UI**: [Streamlit](https://streamlit.io/)  
- **Navigation Menu**: `streamlit-option-menu`  
- **Machine Learning**: Scikit-learn (pre-trained model saved as `.sav`)  
- **Data Handling**: NumPy, Pickle  
- **Visitor Analytics**: Pickle for local storage  

---

## 📂 Project Structure
```
├── heart_disease_model1.sav   # Trained ML model
├── visitor_data.pkl            # Stores visitor count & logs
├── app.py                      # Main Streamlit application code
```

---

## 🚀 How to Run the App
1. **Clone the repository** or save the `app.py` file.  
2. Install dependencies:
   ```bash
   pip install streamlit streamlit-option-menu numpy scikit-learn
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at:
   ```
   http://localhost:8501
   ```

---

## 📊 Machine Learning Model
- The model is trained on the **UCI Heart Disease Dataset**.  
- Algorithms used: (e.g., Logistic Regression / Random Forest).  
- Input features: Age, Sex, CP, Trestbps, Chol, FBS, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal.  
- Output: **Binary Classification** →  
  - `1` = Likely to have heart disease  
  - `0` = Unlikely to have heart disease  

---

## ⚠️ Disclaimer
- This app is **strictly for educational and screening purposes**.  
- It does **not** replace professional medical consultation.  
- The developers are not liable for health-related decisions made based on this app.  

---

## 📸 Screenshots (Optional)
*(You can add screenshots here for visual appeal, e.g., Welcome Page, Prediction Form, Results, Analytics Page)*  

---

## ✨ Future Improvements
- 📌 Deploy app to cloud (Heroku, Streamlit Cloud).  
- 📌 Enhance prediction model with more advanced algorithms.  
- 📌 Add visualization dashboards for input distributions.  
- 📌 Multi-language support.  
- 📌 Integration with wearable device data.  

---

## 👨‍💻 Author
**Enoch Bereka**  
📌 Data Scientist | Biostatistician | ML Enthusiast  
🌍 Passionate about using data science & AI for **healthcare solutions**.  
