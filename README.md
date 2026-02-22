🚨 Job Scam Prediction System

📌 Project Overview
The Job Scam Prediction System is a Machine Learning-based web application designed to detect fraudulent job postings. The system analyzes job descriptions and predicts whether a job listing is Legitimate or Scam, along with a scam probability score.

This project aims to help job seekers avoid financial fraud, identity theft, and misleading job offers by providing an AI-powered risk assessment tool.

🎯 Problem Statement

Online job portals contain thousands of job postings, and many of them are fraudulent. Identifying scam job listings manually is difficult and time-consuming.

The goal of this project is to build an AI model that automatically classifies job postings as Real or Fraudulent using Natural Language Processing (NLP) and Machine Learning techniques.

🧠 Proposed Solution

The system uses text preprocessing and TF-IDF vectorization to convert job descriptions into numerical features. A Multinomial Naive Bayes classifier is trained to detect scam patterns in job postings.

The trained model is deployed using Flask, allowing users to input job descriptions through a web interface and receive instant scam risk predictions.

**⚙️ Technologies Used**

~ Python

~ Scikit-learn

~ TF-IDF Vectorizer

~ Multinomial Naive Bayes

~ Flask (Web Framework)

~ HTML & CSS

~ Pickle (Model Serialization)

**🔍 Model Workflow**

1.Data Collection (Real & Fake Job Posting Dataset)

2.Data Cleaning and Text Preprocessing

3.TF-IDF Feature Extraction

4.Model Training (Naive Bayes)

5.Model Evaluation (Accuracy, Precision, Recall, Confusion Matrix)

6.Model Deployment using Flask

**📊 Model Performance**

->Accuracy: ~91–97% (depending on balancing method)

->Successfully detects high-risk scam job postings

->Provides probability-based risk assessment:

🚨 High Scam Risk

⚠️ Medium Scam Risk

✅ Legitimate Job

**🌍 Social Impact**

This system contributes to society by:

->Protecting job seekers from online fraud

->Reducing financial scams

->Increasing trust in digital recruitment platforms

->Supporting fraud detection in the finance and employment sector
