from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
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
    # Loan_Status: object

# loading the saved model
loan_model = pickle.load(open('model.sav','rb'))

@app.post('/loan_prediction') # used when some one has to give values
def loan_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data) # To convert to dict

    gndr = input_dictionary['Gender']
    mrd = input_dictionary['Married']
    dep = input_dictionary['Dependents']
    edu = input_dictionary['Education']
    selfemp = input_dictionary['Self_Employed']
    aplinc = input_dictionary['ApplicantIncome']
    lnamt = input_dictionary['LoanAmount']
    lnterm = input_dictionary['Loan_Amount_Term']
    cred = input_dictionary['Credit_History']
    ppt = input_dictionary['Property_Area']
    # sts = input_dictionary['Loan_Status']

    input_list = [gndr, mrd, dep, edu, selfemp, aplinc, lnamt, lnterm, cred, ppt]

    prediction = loan_model.predict([input_list])

    if prediction[0] == 0:
        return 'Not Approved'
    else:
        return 'Approved'
    
# should check how to host public API

    
