from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved XGBoost model
model = joblib.load("payments.pkl")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    try:
        features = [
            float(request.form['step']),
            float(request.form['type']),
            float(request.form['amount']),
            float(request.form['oldbalanceOrg']),
            float(request.form['newbalanceOrg']),
            float(request.form['oldbalanceDest']),
            float(request.form['newbalanceDest'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        result = "🚨 Fraud Detected!" if prediction == 1 else "✅ Transaction is Safe."

    except Exception as e:
        result = f"Error in prediction: {e}"

    return render_template("submit.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
