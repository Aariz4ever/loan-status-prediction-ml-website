from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins for simplicity (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ModelInput(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: int 
    Credit_History: float
    Property_Area: int

# Load the saved model
loan_model = pickle.load(open('model.sav', 'rb'))

@app.post('/loan_prediction')
def loan_pred(input_parameters: ModelInput):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    input_list = [
        input_dictionary['Gender'],
        input_dictionary['Married'],
        input_dictionary['Dependents'],
        input_dictionary['Education'],
        input_dictionary['Self_Employed'],
        input_dictionary['ApplicantIncome'],
        input_dictionary['LoanAmount'],
        input_dictionary['Loan_Amount_Term'],
        input_dictionary['Credit_History'],
        input_dictionary['Property_Area'],
    ]

    prediction = loan_model.predict([input_list])

    if prediction[0] == 0:
        return {'prediction': 'Not Approved'}
    else:
        return {'prediction': 'Approved'}