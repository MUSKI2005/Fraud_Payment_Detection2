# Folder Structure Explanation

This project is organized into logical phases to mirror real-world ML workflows:

1. **Project Initiation and Planning Phase**: Contains all planning and proposal files.
2. **Data Collection and Preprocessing Phase**: Handles data cleaning, transformation, and exploration.
3. **Model Development Phase**: Contains model training and evaluation notebooks.
4. **Model Optimization Phase**: Includes comparison of models and the final trained `.pkl` file.
5. **Project Execution**: Web application files and deployment-ready scripts.


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
