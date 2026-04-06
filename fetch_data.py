# CUSTOMER CHURN PREDICTION MODEL

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import sys
sys.stdout.reconfigure(encoding='utf-8')
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_auc_score
import plotext as pltxt
import joblib
from xgboost import XGBClassifier
import os
from datetime import datetime

# STEP 1: LOAD DATA

df = pd.read_csv("Telco_Cusomer_Churn.csv")

print("Dataset Loaded Successfully!\n")
print(df.head())

# STEP 2: DATA CLEANING

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Convert Churn to binary
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Drop missing values
df.dropna(inplace=True)

# Drop unnecessary column
df.drop(columns=['customerID'], inplace=True)

print("\nData Cleaning Done!")

# STEP 3: FEATURE ENGINEERING

# Avg spend feature
df['avg_spend'] = df['TotalCharges'] / (df['tenure'] + 1)

# Tenure groups
df['tenure_group'] = pd.cut(df['tenure'],
                           bins=[0,12,24,60,100],
                           labels=['New','Mid','Loyal','Old'])

print("\nFeature Engineering Done!")

# STEP 4: ENCODING

# One-hot encoding
df = pd.get_dummies(df, drop_first=True)

print("\nEncoding Done!")

# STEP 5: SPLIT DATA

X = df.drop(columns=['Churn'])
y = df['Churn']

print("\nChurn Distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split Done!")

# STEP 6: MODEL TRAINING
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
}

best_model = None
best_accuracy = 0
best_model_name = ""

best_score = -1

model_metrics = {}

print("\n=== MODEL COMPARISON ===\n")

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]  
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_prob)
    cv_score = cross_val_score(model, X, y, cv=5, scoring='roc_auc').mean()

    print(f"{name} -> Accuracy: {acc:.4f} | ROC-AUC: {roc:.4f} | CV: {cv_score:.4f}")

    # Save metrics
    model_metrics[name] = {
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1": f1,
        "ROC": roc
    }

    # Find best model
    if roc > best_score:
        best_score = roc
        best_model = model
        best_model_name = name

# BEST MODEL

print("\n=== BEST MODEL ===\n")
print(f"Best Model: {best_model_name}")
print(f"Best ROC-AUC: {best_score:.4f}")

print("\nModel Training Completed!")

# STEP 7: PREDICTIONS

y_pred = best_model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# STEP 8: EVALUATION

print("\nMODEL PERFORMANCE:\n")

y_pred = best_model.predict(X_test)

print("\n=== FINAL MODEL PERFORMANCE ===\n")
print(f"Best Model : {best_model_name}")
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# STEP 9: FEATURE IMPORTANCE

if hasattr(best_model, "feature_importances_"):
    importances = best_model.feature_importances_
    
    features = X.columns
    indices = np.argsort(importances)[-10:]

    top_features = [features[i] for i in indices]
    top_importances = [importances[i] for i in indices]

    plt.barh(top_features, top_importances)
    plt.title("Top Features")
    plt.show()

# ROC CURVE IN TERMINAL

y_prob = best_model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr, label="ROC Curve")
plt.plot([0,1], [0,1], label="Random", marker="x")
plt.title("ROC Curve")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.show()

#  MODEL MONITORING SYSTEM

def check_model_health():
    print("\nChecking model health...\n")

    if not os.path.exists("prediction_logs.csv"):
        print("No logs found yet.")
        return

    logs = pd.read_csv("prediction_logs.csv")

    #  Accuracy Tracking 
    high_risk = logs[logs["probability"] > 0.5]

    if len(high_risk) > 0:
        avg_risk = high_risk["probability"].mean()
        print(f"Average predicted risk: {avg_risk:.2f}")
    else:
        print("No high-risk predictions yet.")

    #  DATA DRIFT CHECK
    if os.path.exists("baseline_stats.pkl"):
        baseline = joblib.load("baseline_stats.pkl")

        current_data = pd.read_csv("dummy_customers.csv")
        current_data = pd.get_dummies(current_data)

        # Match columns
        for col in baseline.columns:
            if col not in current_data.columns:
                current_data[col] = 0

        current_data = current_data[baseline.columns]

        current_stats = current_data.describe()

        drift = abs(current_stats - baseline)

        drift_score = drift.mean().mean()

        print(f"Drift Score: {drift_score:.4f}")

        if drift_score > 0.5:
            print("⚠️ Data Drift Detected! Retraining Recommended")
            retrain_model()
        else:
            print("✅ Model Stable")

#  AUTO RETRAINING

def retrain_model():
    print("\n🔄 Retraining model...\n")

    df = pd.read_csv(r"C:\Aparaitech\Customer_churn_system\Telco_Cusomer_Churn.csv")

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df.dropna(inplace=True)
    df.drop(columns=['customerID'], inplace=True)
    
    df['avg_spend'] = df['TotalCharges'] / (df['tenure'] + 1)

    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0,12,24,60,100],
        labels=['New','Mid','Loyal','Old']
    )

    df = pd.get_dummies(df,drop_first=True)

    X = df.drop(columns=['Churn'])
    y = df['Churn']

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X, y)

    joblib.dump(model, "churn_model.pkl")

    print("✅ Model Retrained & Saved Successfully!")

print("\n Project Completed Successfully!")

joblib.dump(models, "all_models.pkl")   # Save ALL models
joblib.dump(best_model, "churn_model.pkl")  
joblib.dump(model_metrics,"model_metrics.pkl")

feature_names = X_train.columns 
joblib.dump(feature_names, "feature_names.pkl")

joblib.dump(X_test, "X_test.pkl")
joblib.dump(y_test, "y_test.pkl")

#  Save baseline stats 
baseline_stats = X_train.describe()
joblib.dump(baseline_stats, "baseline_stats.pkl")

print("Baseline stats saved!")

print("All Files saved successfully!")
