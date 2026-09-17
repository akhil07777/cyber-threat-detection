
# AI-Based Cybersecurity Threat Detection Platform

An AI-powered web application for detecting and analyzing potential cybersecurity threats in network-traffic data using Machine Learning.

## 📌 Project Overview

The AI-Based Cybersecurity Threat Detection Platform is a web-based cybersecurity application developed using Flask and Machine Learning.

The system analyzes structured network-traffic data and classifies each record as either **Normal** or **Attack**.

The application also calculates prediction confidence, assigns a risk level, stores the results in MongoDB Atlas, and provides dashboards and reports for analysis.

This project was developed as an internship project to demonstrate the integration of Artificial Intelligence, Machine Learning, Web Development, and Database Management in a cybersecurity application.

## 🎯 Objectives

- Analyze network-traffic data using Machine Learning.
- Detect potential malicious network activity.
- Classify traffic as Normal or Attack.
- Calculate prediction confidence.
- Assign risk levels based on attack confidence.
- Store prediction results in a database.
- Provide dashboards and reports for analysis.
- Provide a foundation for future real-time cybersecurity monitoring.

## 🏗️ System Workflow

User Login
    ↓
Upload Network-Traffic Data
    ↓
Data Preprocessing
    ↓
Categorical Feature Encoding
    ↓
Random Forest Model
    ↓
Normal / Attack Prediction
    ↓
Confidence Calculation
    ↓
Risk Level Assignment
    ↓
MongoDB Atlas
    ↓
Dashboard & Reports
    ↓
Security Analysis

## 🤖 Machine Learning

The project uses the **Random Forest Classifier** for network-traffic classification.

### Dataset

The model is trained using the **NSL-KDD dataset**, with KDDTrain+ used as the training data.

The dataset contains network-connection features such as:

- Duration
- Protocol type
- Service
- Flag
- Source bytes
- Destination bytes
- Logged-in status
- Connection statistics
- Error and service-rate statistics

The target label is used to classify traffic into:

- Normal
- Attack

### Preprocessing

Before prediction, the input data goes through preprocessing:

1. Unnecessary fields such as label and difficulty are removed where applicable.
2. Categorical features are encoded.
3. Features are arranged in the format expected by the trained model.
4. The processed data is passed to the Random Forest classifier.

### Prediction

The Random Forest model provides:

Prediction → Normal / Attack

The `predict_proba()` function is used to obtain the probability associated with the prediction.

This probability is used as the confidence score.

## ⚠️ Risk Classification

For detected attack records, the system assigns a risk level based on the attack confidence.

| Condition | Risk Level |
|---|---|
| Attack confidence ≥ 95% | Critical |
| Attack confidence ≥ 85% | High |
| Attack confidence ≥ 70% | Medium |
| Attack confidence < 70% | Low |
| Normal prediction | Low |

The risk level helps prioritize records that may require further investigation.

## 🖥️ Application Modules

The application consists of the following major modules.

### 1. Authentication

- User registration
- User login
- Session-based authentication

### 2. Data Upload

- Accepts structured network-traffic data.
- Validates the uploaded file.
- Reads the data using Pandas.

### 3. Prediction

- Preprocesses the input.
- Encodes categorical features.
- Uses the trained Random Forest model.
- Generates Normal/Attack predictions.

### 4. Risk Analysis

- Calculates prediction confidence.
- Assigns a risk level based on the confidence.

### 5. Database

MongoDB Atlas is used to store:

- User information
- Upload information
- Prediction reports

### 6. Dashboard

The dashboard provides an overview of:

- Total records
- Attack records
- Normal records
- Recent uploads
- Prediction statistics

### 7. Reports

The reports section allows users to:

- View generated reports.
- Review prediction results.
- Inspect individual network records.
- Identify higher-risk records for further investigation.

## 🛠️ Technology Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- Random Forest
- Pandas
- NumPy
- Joblib

### Database

- MongoDB Atlas

### Frontend

- HTML
- CSS
- JavaScript
- Bootstrap
- Chart.js

### Development & Deployment

- Git
- GitHub
- Render


