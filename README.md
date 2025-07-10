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
├── Project Initiation and Planning Phase/
│   ├── Project_Proposal.md               # Objective & problem statement
│   ├── Tech_Stack_and_Tools.md           # Languages, libraries, frameworks
│   ├── Timeline.md                       # Weekly plan (if applicable)
│   └── Project_Structure_Notes.md        # Description of folder organization
│
├── Data Collection and Preprocessing Phase/
│   ├── data_preprocessing.ipynb          # Data cleaning & preprocessing code
│   └── data/
│       └── dataset.md                    # Dataset source & description (NO raw CSV)
│
├── Model Development Phase/
│   └── model_training.ipynb              # Training all required models
│                                         # (Random Forest, DT, XGBoost, etc.)
│
├── Model Optimization Phase/
│   ├── model_comparison.ipynb            # Evaluation, comparison, plots
│   └── payments.pkl                      # Final/best-performing model file
│
├── Project Execution/
│   ├── flask/
│   │   ├── app.py                        # Main Flask app (local)
│   │   ├── app_ibm.py                    # IBM deployment version (if used)
│   │   ├── payments.pkl                  # Deployed model (can copy from above)
│   │
│   │   ├── static/
│   │   │   └── styles.css                # Web app styling
│   │
│   │   └── templates/
│   │       ├── home.html                 # Landing page
│   │       ├── predict.html              # Input form for transaction data
│   │       └── submit.html               # Output page (fraud/not fraud)
│   │
│   └── requirements.txt                  # All necessary Python packages
│
├── README.md                             # Main project guide (at root level)
