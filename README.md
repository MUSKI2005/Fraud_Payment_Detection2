# Fraud_Payment_Detection2
# Fraud Payment Detection Web App

A machine learning-based web application to detect fraudulent transactions using user input. Built with **Flask** for the backend and a trained **scikit-learn model** for predictions.

---

## Features

- Predicts whether a payment is fraudulent or not.
- Built using a trained machine learning model (e.g., Logistic Regression, Random Forest).
- Clean and responsive web interface.
- Lightweight Flask backend.

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas & NumPy
- HTML/CSS (Bootstrap optional)
- Jupyter Notebook (for preprocessing & training)

---
# STRUCTURE
Fraud_Payment_Detection2/
│
├── data/                            #  Datasets (for local use only)
│   └── dataset.md                   #  Dataset info or markdown (not actual data CSV)
│
├── flask/                           #  Main Flask app folder
│   ├── app.py                       #  Main Flask application (local model)
│   ├── app_ibm.py                   #  Flask app version for IBM Cloud (optional)
│   ├── payments.pkl                 #  Trained model file
│
│   ├── static/                      #  Static files (CSS, JS, images)
│   │   └── styles.css               #  CSS for styling
│
│   └── templates/                   #  HTML templates
│       ├── home.html                #  Welcome/Homepage
│       ├── predict.html             #  Input form for fraud detection
│       └── submit.html              #  Result display page
│
├── data_preprocessing.ipynb         #  Notebook for data cleaning & feature prep
├── model_training.ipynb             #  Model training, evaluation, and saving
│
├── requirements.txt                 #  Python packages required
├── README.md                        #  Project description & instructions
