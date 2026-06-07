# 🌸 **Iris Flower Classification Using Machine Learning**

---

# 📖 Project Description

The Iris Flower Classification project is a supervised machine learning classification problem where the objective is to predict the species of an iris flower based on its physical measurements.

Using sepal length, sepal width, petal length, and petal width, the model classifies flowers into one of three species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

This project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model training, evaluation, and prediction.

---

# 🎯 Business Objective

Develop a machine learning model capable of accurately identifying iris flower species based on flower measurements.

---

# 📂 Dataset Information

### Features

| Feature      | Description           |
| ------------ | --------------------- |
| Sepal Length | Length of sepal in cm |
| Sepal Width  | Width of sepal in cm  |
| Petal Length | Length of petal in cm |
| Petal Width  | Width of petal in cm  |

### Target Variable

| Species    |
| ---------- |
| Setosa     |
| Versicolor |
| Virginica  |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

# 🔄 Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Model Building
      ↓
Model Evaluation
      ↓
Prediction
```

---

# 📊 EDA Insights

## 1. Species Distribution

### Insight:

The dataset is balanced with an equal number of observations for all three flower species.

### Business Impact:

Balanced datasets help machine learning models avoid bias toward a particular class.

---

## 2. Petal Length Distribution

### Insight:

Petal length varies significantly across species.

### Business Impact:

Petal length is one of the strongest predictors of flower species.

---

## 3. Petal Width Distribution

### Insight:

Setosa flowers have much smaller petal widths compared to the other species.

### Business Impact:

Petal width helps separate Setosa flowers with high accuracy.

---

## 4. Sepal Length Analysis

### Insight:

Virginica generally exhibits larger sepal lengths.

### Business Impact:

Useful in distinguishing Virginica from other species.

---

## 5. Correlation Analysis

### Insight:

Petal Length and Petal Width show strong positive correlation.

### Business Impact:

These features contribute significantly to classification performance.

---

# 📈 Visual-wise Insights

## Histogram – Petal Length

**Observation:**
Three distinct distributions are visible for the species.

**Insight:**
Petal Length is highly effective for classification.

---

## Histogram – Petal Width

**Observation:**
Setosa occupies a separate range.

**Insight:**
Minimal overlap makes classification easier.

---

## Scatter Plot

**Observation:**
Species form separate clusters.

**Insight:**
The dataset is naturally separable.

---

## Pair Plot

**Observation:**
Petal-related features provide clear species separation.

**Insight:**
Petal measurements are more informative than sepal measurements.

---

## Heatmap

**Observation:**
Strong correlation between petal length and petal width.

**Insight:**
These variables carry significant predictive power.

---

# 🤖 Machine Learning Models

### Logistic Regression

* Accuracy: ~95%+

### K-Nearest Neighbors

* Accuracy: ~97%+

### Decision Tree

* Accuracy: ~95–100%

### Random Forest

* Accuracy: ~97–100%

### Support Vector Machine

* Accuracy: ~97–100%

---

# 📊 Model Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

---

### Insight 1

Petal Length and Petal Width were identified as the most influential features in determining iris flower species.

### Insight 2

The dataset exhibited well-separated class boundaries, enabling machine learning models to achieve very high classification accuracy.

### Insight 3

Random Forest and Support Vector Machine models delivered the best performance, achieving near-perfect classification results.

---

# 🚀 Streamlit App Features

### User Inputs

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Outputs

* Predicted Species
* Prediction Confidence
* Model Accuracy

### Extra Features

* Dataset Preview
* EDA Visualizations
* Feature Importance Plot
* Model Performance Metrics

---
### Project Highlights

✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Feature Correlation Analysis

✅ Multiple Machine Learning Models

✅ Model Evaluation

✅ Prediction System

✅ Streamlit Deployment


---

# ⭐ Future Enhancements

* Deploy using Streamlit Cloud
* Add model comparison dashboard
* Implement hyperparameter tuning
* Create API integration using Flask/FastAPI
* Add real-time prediction interface
