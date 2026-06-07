import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide"
)

# Load Dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

species_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# Load Model
model = pickle.load(open("iris_model.pkl", "rb"))

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Prediction",
        "Dataset",
        "EDA",
        "Model Performance"
    ]
)

# Prediction Page
if page == "Prediction":

    st.title("🌸 Iris Flower Classification")

    st.write(
        "Enter flower measurements to predict species."
    )

    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.slider(
            "Sepal Length (cm)",
            4.0, 8.0, 5.8
        )

        sepal_width = st.slider(
            "Sepal Width (cm)",
            2.0, 5.0, 3.0
        )

    with col2:
        petal_length = st.slider(
            "Petal Length (cm)",
            1.0, 7.0, 4.0
        )

        petal_width = st.slider(
            "Petal Width (cm)",
            0.1, 3.0, 1.2
        )

    if st.button("Predict"):

        features = np.array([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)

        st.success(
            f"Predicted Species: {species_names[prediction]}"
        )

        st.write(
            f"Confidence Score: {np.max(probability)*100:.2f}%"
        )

# Dataset Page
elif page == "Dataset":

    st.title("📊 Dataset Overview")

    st.write(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Statistical Summary")
    st.write(df.describe())

# EDA Page
elif page == "EDA":

    st.title("📈 Exploratory Data Analysis")

    st.subheader("Feature Distribution")

    fig, ax = plt.subplots(figsize=(10,6))
    df.hist(figsize=(10,8))
    st.pyplot(plt)

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="Blues")
    st.pyplot(fig)

# Model Performance
elif page == "Model Performance":

    st.title("🤖 Model Performance")

    X = df.drop("species", axis=1)
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    pred = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        pred
    )

    st.metric(
        "Model Accuracy",
        f"{accuracy*100:.2f}%"
    )