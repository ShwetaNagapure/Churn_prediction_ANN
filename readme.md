#  Customer Churn Prediction using ANN

 **Live Demo:**
https://churnpredictionann-gkeeofwtmgadkkbanzspxg.streamlit.app/

This project is a **Customer Churn Prediction Web Application** built
using **Artificial Neural Networks (ANN)** with **TensorFlow/Keras** and
deployed using **Streamlit**.

The application predicts whether a customer is **likely to churn or
not** based on banking and demographic features.

------------------------------------------------------------------------

##  Features

-   Interactive Streamlit UI
-   ANN-based churn prediction
-   Real-time probability output
-   Uses trained scaler and encoders
-   Deployment-ready

------------------------------------------------------------------------

##  Model Overview

-   Algorithm: Artificial Neural Network (ANN)
-   Framework: TensorFlow / Keras
-   Problem Type: Binary Classification
-   Output:
    -   1 → Customer likely to churn
    -   0 → Customer not likely to churn

------------------------------------------------------------------------

##  Project Structure

    Churn_prediction_ANN/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── model/
        ├── churn_prediction_model.keras
        ├── scaler.pkl
        ├── label_encoder.pkl
        └── onehot_encoder.pkl

------------------------------------------------------------------------

##  Input Features

-   Credit Score
-   Geography
-   Gender
-   Age
-   Tenure
-   Balance
-   Number of Products
-   Credit Card
-   Active Member
-   Estimated Salary

------------------------------------------------------------------------

## Run Locally

``` bash
git clone https://github.com/ShwetaNagapure/Churn_prediction_ANN.git
cd Churn_prediction_ANN
pip install -r requirements.txt
streamlit run app.py
```

------------------------------------------------------------------------

## ☁️ Hosting

This application is hosted on **Streamlit Cloud**.

🔗 Live App:\
https://churnpredictionann-gkeeofwtmgadkkbanzspxg.streamlit.app/



⭐ If you like this project, consider giving it a star!
