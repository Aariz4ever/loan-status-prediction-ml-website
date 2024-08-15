import json
import requests

url = "http://127.0.0.1:8000/loan_prediction"  # api_server/endpoint mentioned in @app.post

input_data_for_model = {
    'Gender': 1,
    'Married': 0,
    'Dependents': 0,
    'Education': 0,
    'Self_Employed': 0,
    'ApplicantIncome': 5849,
    'LoanAmount': 126.0,
    'Loan_Amount_Term': 5, 
    'Credit_History': 1.0,
    'Property_Area': 2,
}

# importing json to API
input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text) # return values are string