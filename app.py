import streamlit as st 
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pickle
import tensorflow as tf

model=tf.keras.models.load_model("model/churn_prediction_model.keras")

# load the encoder and scaler 
with open("model/label_encoder.pkl","rb") as file:
    label_encoder=pickle.load(file)
with open("model/onehot_encoder.pkl","rb") as file:
    onehot_encoder=pickle.load(file)
with open("model/scaler.pkl","rb") as file:
    scaler=pickle.load(file)

##streamlit app

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score")
geography = st.selectbox("Geography",onehot_encoder.categories_[0])
gender = st.selectbox("Gender",label_encoder.classes_)
age = st.number_input("Age", min_value=18, max_value=100)
tenure = st.number_input("Tenure (Years)", min_value=0, max_value=20)
balance = st.number_input("Balance", min_value=0.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary")