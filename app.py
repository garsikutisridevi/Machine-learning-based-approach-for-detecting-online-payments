from flask import Flask, render_template, request
from zlog import predicted 
import joblib
import numpy as np 

app = Flask(__name__, static_url_path='/static')

# Load trained model 
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transaction')
def transaction():
    return render_template('transactions.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve user inputs from the form
    transaction_type = request.form.get('transaction-type')
    amount = float(request.form.get('amount'))
    old_balance = float(request.form.get('old-balance'))
    new_balance = float(request.form.get('new-balance'))
    step = int(request.form.get('step'))
    old_balance_dest = float(request.form.get('old-balance-dest'))
    new_balance_dest = float(request.form.get('new-balance-dest'))
    prediction = predicted(transaction_type, amount, old_balance, new_balance, step, old_balance_dest, new_balance_dest)

    result = "Fraud" if prediction == 1 else "Non-fraud"
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)










