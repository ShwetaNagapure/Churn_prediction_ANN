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

##user input 
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

## prepraring input data 
df_unseen= pd.DataFrame({
    'CreditScore':[credit_score],
    'Geography':[geography],
    'Gender':[label_encoder.transform([gender])[0]],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_products],
    "HasCrCard":[has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
})

##one hot encoding for the geography 

geo_encoded = onehot_encoder.transform(df_unseen[['Geography']])
# Create a DataFrame from the encoded data with appropriate column names
geo_df = pd.DataFrame(geo_encoded, columns=onehot_encoder.get_feature_names_out(['Geography']))

df_unseen = pd.concat([df_unseen, geo_df], axis=1)
df_unseen.drop('Geography',axis=1,inplace=True)
##scale the unseen data 

df_unseen_scaled=scaler.transform(df_unseen)

##prediction
predict=model.predict(df_unseen_scaled)
prediction_prob =predict[0][0]

if prediction_prob >0.5:
    st.writ("the customer is likely to churn",prediction_prob)
else:
    st.write("the customer is not likely to churn",prediction_prob)