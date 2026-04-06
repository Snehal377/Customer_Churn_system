📌 Project Title

Customer Churn Prediction System 

📖 Overview

Customer churn is one of the most critical problems in telecom and subscription-based businesses. 
This project builds a complete end-to-end Machine Learning system that not only predicts churn but 
also simulates real-world production features like API deployment, monitoring, alerting, 
and CRM integration.

This is not just a model — it is a full data science product.

🎯 Problem Statement

Predict whether a customer will churn (leave the service) based on historical data 
and enable businesses to take proactive actions.

📂 Dataset

Telecom Customer Dataset (~7,043 records)

Features include:

Customer demographics (Gender, Senior Citizen)
Account info (Tenure, Contract)
Services (Internet, Phone, Streaming)
Financials (MonthlyCharges, TotalCharges)

⚙️ Tech Stack

 Machine Learning :
 
Logistic Regression
Random Forest
Gradient Boosting
XGBoost

 Data Processing :

Pandas, NumPy
Feature Engineering
One-Hot Encoding

 Backend (API) :

FastAPI (Real-time prediction API)

 Frontend Dashboard :
 
Streamlit
Plotly (interactive charts)
Seaborn & Matplotlib

 Deployment Tools:
 
Joblib (model saving/loading)

CSV-based logging (pipeline simulation) :

 End-to-End Pipeline :
 
1️⃣ Data Preprocessing :

Handled missing values
Converted data types
Removed irrelevant columns

2️⃣ Feature Engineering :

Created avg_spend feature
Created tenure_group segmentation

3️⃣ Encoding :

Applied One-Hot Encoding

4️⃣ Model Training & Selection :

Trained 4 ML models
Compared using:
Accuracy
Precision
Recall
F1 Score
ROC-AUC

👉 Best model selected based on ROC-AUC score

🤖 Model Performance System :

Automatic comparison of multiple models
Best model selection logic
Saved:
Best model
All models
Metrics
Feature names
 
🔮 Prediction System :

✔️ Two Modes:
API-based Prediction (Real-time)
Manual Input Prediction (UI)

Output:

Prediction (Churn / No Churn)

Probability Score

Risk Level:
🟢 Low
🟡 Medium
🔴 High

FastAPI (Real-Time API):

Endpoint:
GET /predict/{customer_id}

Features:

Fetch customer from dataset

Apply preprocessing + feature engineering

Predict churn

Return JSON response

Example Response:
{
  "customerID": "7795-CFOCW",
  "prediction": 1,
  "probability": 0.84
}

🚨 Monitoring & Logging System :

✔️ Prediction Logs

Stored in prediction_logs.csv

Tracks:

Customer ID
Prediction
Probability
Timestamp

✔️ Alert System :

Triggered when probability > 0.8
Stored in alerts.csv

✔️ CRM Integration (Simulated) :

High-risk customers converted into tasks
Stored in crm_tasks.csv 

📡 Model Monitoring (Advanced Feature) :

✔️ Model Health Check  :

 Tracks average risk
 
✔️ Data Drift Detection :

Compares current vs baseline statistics
Generates drift score

✔️ Auto Retraining :

Triggered when drift exceeds threshold
Retrains and updates model automatically 

📊 Streamlit Dashboard Features :

🏠 Overview Page
Business problem explanation
KPIs:
Total Customers
Churn Rate
Revenue Impact

🔮 Prediction Page :

API-based prediction
Manual input prediction
Gauge chart for churn risk
Feature importance display 

📊 Analytics Page :

Interactive filters
KPI cards
Visualizations:
Churn by contract
Payment method analysis
Tenure distribution
Correlation heatmap 

⚙️ Model Comparison Page :

Compare all models
ROC-AUC visualization
Performance metrics:
Accuracy
Precision
Recall
F1

🚨 Monitoring Dashboard :

Prediction logs
High-risk alerts
CRM tasks
Risk distribution charts 

🧱 Scalable Architecture (Simulation) :

Modular pipeline design

Ready for:
Kafka (streaming)
BigQuery (data warehouse)
Real-time system simulation using CSV

💡 Key Highlights 

✅ End-to-End ML Pipeline
✅ Real-Time API (FastAPI)
✅ Interactive Dashboard (Streamlit)
✅ Model Monitoring System
✅ Data Drift Detection
✅ Auto Retraining Logic
✅ Business Rule Engine
✅ CRM Integration Simulation

🎯 Conclusion

This project demonstrates how to move beyond basic machine learning and build a production-ready 
AI system. It combines data science, backend engineering, and business logic, 
making it highly relevant for real-world applications.
