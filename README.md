# ❤️ Heart Disease Prediction Project

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Health%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.9+-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

Heart disease remains one of the leading causes of morbidity and mortality worldwide. Early detection is crucial in reducing risks and improving patient outcomes. This project applies **machine learning techniques** to predict the likelihood of heart disease based on patient characteristics and clinical data.

The study compares multiple models — **Logistic Regression, Decision Tree, Random Forest, Naive Bayes, and Support Vector Machine (SVM)** — and selects the best-performing one to create a **clinician-friendly prediction scoring tool**.

---

## 🎯 Study Objectives

### **General Objective**

* To develop and evaluate predictive models for heart disease and determine the most effective model for accurate early detection and clinical decision-making.

### **Specific Objectives**

1. To identify and describe the socio-demographic and clinical risk factors associated with heart disease in the study population.
2. To build predictive models for heart disease using Logistic Regression, Decision Tree, Random Forest, Naive Bayes, and Support Vector Machine (SVM).
3. To evaluate and compare the performance of the models using **accuracy, sensitivity, specificity, precision, F1-score, and ROC-AUC**.
4. To select the best-performing model for heart disease prediction and develop a **scoring system/tool** for clinicians to facilitate timely diagnosis and intervention.
5. To provide recommendations on how predictive analytics can be integrated into healthcare systems for early identification and management of heart disease.

---

## ❓ Research Questions

1. What socio-demographic and clinical risk factors are significantly associated with heart disease?
2. How do different machine learning models (Logistic Regression, Decision Tree, Random Forest, Naive Bayes, and SVM) perform in predicting heart disease?
3. Which model demonstrates the best predictive performance based on accuracy, sensitivity, specificity, F1-score, and ROC-AUC?
4. Can the best-performing model be developed into a scoring system/tool for clinical use?

---

## 🔬 Hypotheses

* **Null Hypothesis (H₀):** There is no significant difference in predictive performance among the machine learning models used to predict heart disease.
* **Alternative Hypothesis (H₁):** There is a significant difference in predictive performance among the machine learning models, and one model outperforms the others in predicting heart disease.

---

## 📊 Dataset

* **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease) (or Kaggle equivalent)
* **Features:** Age, sex, chest pain type, blood pressure, cholesterol, fasting blood sugar, resting ECG, maximum heart rate, exercise-induced angina, ST depression, slope of ST segment, number of major vessels, thalassemia.
* **Target:** Presence or absence of heart disease (binary outcome).

---

## ⚙️ Methodology

### 1. **Data Preprocessing**

* Handling missing values
* Encoding categorical variables
* Feature scaling/normalization
* Train-test split

### 2. **Model Development**

* Logistic Regression
* Decision Tree
* Random Forest
* Naive Bayes
* Support Vector Machine (SVM)

### 3. **Model Evaluation**

* Confusion Matrix
* Accuracy, Sensitivity (Recall), Specificity, Precision
* F1-Score
* ROC Curve and AUC

### 4. **Model Selection**

* Compare results across models
* Select best-performing model
* Develop clinical scoring tool

---

## 📈 Results (Illustrative Example)

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression | 85.7%    | 0.83      | 0.87   | 0.85     | 0.90    |
| Decision Tree       | 78.9%    | 0.76      | 0.80   | 0.78     | 0.81    |
| Random Forest       | 84.2%    | 0.82      | 0.85   | 0.83     | 0.88    |
| Naive Bayes         | 79.4%    | 0.77      | 0.79   | 0.78     | 0.82    |
| SVM                 | 83.5%    | 0.81      | 0.84   | 0.82     | 0.87    |

👉 **Logistic Regression** showed the best predictive performance.

---

## 🏥 Clinical Implications

* The logistic regression model was developed into a **risk scoring system**.
* Clinicians can input patient data to obtain a risk score.
* Supports early intervention and personalized treatment strategies.

---

## 💻 Tools & Libraries

* **Programming Language:** Python
* **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn

---

## 🚀 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/username/heart-disease-prediction.git
cd heart-disease-prediction

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Heart_Disease_Prediction.ipynb
```

---

## 📚 References

1. UCI Machine Learning Repository: Heart Disease Dataset
2. WHO. Cardiovascular diseases (CVDs). World Health Organization.
3. Kuhn, M., & Johnson, K. (2013). *Applied Predictive Modeling*. Springer.

---

## 📌 Author

👤 **Enoch Bereka**
📧 [Email](mailto:youremail@example.com) | 🌐 [LinkedIn](https://linkedin.com/in/yourprofile) | 🐦 [Twitter](https://twitter.com/yourprofile)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

✨ *If you find this useful, give it a ⭐ on GitHub!*
