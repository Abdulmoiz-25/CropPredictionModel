# 🌾 Crop Prediction Model using Machine Learning

A machine learning model that predicts the **most suitable crop to grow** based on soil and environmental conditions such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

---

## 📽️ Demo

- ▶️ **YouTube Video**: [Watch Now]([https://youtu.be/ud1yQbr9MZs](https://youtu.be/xB0-W7MdBtk?si=rF2yRFDB6VstpotD])  
- 🌐 **Web App**: [Try the Streamlit App](https://croppredictionmodel-gyoyh5nz6pybyf4naqja4i.streamlit.app/)

---

## 🧰 Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Jupyter Notebook  
- Machine Learning Models:  
  - Random Forest  
  - Decision Tree  
  - Logistic Regression  
- Streamlit 🌐 (for UI deployment)

---

## 📁 Dataset

**Name:** Crop Recommendation Dataset  
**Source:** Kaggle  
**Format:** CSV

### 📊 Features:

| Feature     | Description                       |
|-------------|---------------------------------|
| Nitrogen    | Nitrogen content in the soil    |
| Phosphorus  | Phosphorus content in the soil  |
| Potassium   | Potassium content in the soil   |
| Temperature | Average temperature in °C       |
| Humidity    | Relative humidity in %          |
| pH          | Acidity or alkalinity of soil   |
| Rainfall    | Rainfall in mm                  |

🎯 **Target:** Crop label (e.g., rice, maize, mungbean, etc.)

---

## 📌 Project Overview

This project predicts the best crop to grow given environmental and soil inputs.  
The end-to-end ML pipeline includes:  
1. Dataset loading and preprocessing  
2. Exploratory Data Analysis  
3. Model selection and evaluation  
4. Deployment via Streamlit

---

## 📊 Visualizations

Key visualizations include:  
- 🔥 Heatmaps for correlation  
- 📊 Feature distribution plots  
- 📈 Accuracy bar charts for model comparison  
- 🔢 Confusion matrices  

(All available in the Jupyter notebook)

---

## 🧪 Model Training & Evaluation

### ✅ Models Trained:

- Logistic Regression  
- Decision Tree  
- Random Forest (best performance)  

### 📈 Evaluation Metrics:

- Accuracy Score  
- Confusion Matrix  
- Classification Report  

✅ **Best Performing Model:** Random Forest

---

## 🧠 Insights

- 🌡️ Temperature and rainfall are strong predictors  
- 🍌 Crops like grapes and bananas prefer higher humidity and rainfall  
- 🧪 Acidic soils (low pH) favor crops like watermelon

---

## 🔗 Important Links

- 📂 **GitHub Repo:** [CropPredictionModel](https://github.com/Abdulmoiz-25/CropPredictionModel.git)  
- ▶️ **YouTube Demo:** [Watch here]([https://youtu.be/ud1yQbr9MZs](https://youtu.be/xB0-W7MdBtk?si=rF2yRFDB6VstpotD])  
- 🌐 **Streamlit App:** [Try Now](https://croppredictionmodel-gyoyh5nz6pybyf4naqja4i.streamlit.app/)

---

## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Matplotlib](https://matplotlib.org/)  
- [Seaborn](https://seaborn.pydata.org/)  
- [Original Dataset – Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Abdulmoiz-25/CropPredictionModel.git

# Navigate into the project directory
cd CropPredictionModel

# Run Jupyter Notebook
jupyter notebook



