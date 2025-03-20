# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uKyzJJcBoTpWB5AA_3dHWLb-BcKbi4lw
"""

import streamlit as st
import pickle
import numpy as np
import joblib
!pip install joblib


# Load model dari file pickle
with open("iris_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Judul aplikasi
st.title("Iris Flower Prediction App")
st.write("Masukkan ukuran bunga untuk mendapatkan prediksi spesies.")

# Input fitur dari pengguna
sepal_length = st.number_input("Sepal Length (cm)", min_value=4.0, max_value=8.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=5.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=7.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, step=0.1)

# Tombol prediksi
if st.button("Predict"):
    # Membuat array input untuk model
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Prediksi spesies
    prediction = model.predict(input_features)
    species_dict = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    predicted_species = species_dict[prediction[0]]

    # Tampilkan hasil prediksi
    st.success(f"Model memprediksi bunga ini adalah **{predicted_species}**")
