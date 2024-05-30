from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import time
#import pandas as pd
import loan_app.tests as tests
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



def index(request):
    
    return render(request, 'loan_app/home.html')

def fun():
    societies = sorted(fun['Society'].unique()) 
    locations = sorted(fun['Loc'].unique())
    return render('loan_app/index.html', societies=societies, locations=locations)


@login_required
def predict_form(request):
    Key = tests.ATTRIBUTE
    OPENAI_API_KEY = "sk-proj-k9w727P89E3hJnFia9DIT3BlbkFJkyLfOofiUTpQS6YVEFUT"
    tests.openai.api_key = Key
    client = tests.openai.OpenAI(api_key=OPENAI_API_KEY)
    if request.method == "POST":
        Credit_Score = request.POST.get("Credit_Score") 
        Income = request.POST.get("Income") 
        Employment_Status = request.POST.get("Employment_Status")
        Debt_to_Income_Ratio = request.POST.get("Debt_to_Income_Ratio")
        Loan_Amount = request.POST.get("Loan_Amount")
        Loan_Term = request.POST.get("Loan_Term")
        Payment_History = request.POST.get("Payment_History")
        Age = request.POST.get("Age")
        Loan_Purpose = request.POST.get("Loan_Purpose")
        Assets = request.POST.get("Assets")
        Savings = request.POST.get("Savings")
        Housing_Status = request.POST.get("Housing_Status")
        Marital_Status = request.POST.get("Marital_Status")
        Education_Level = request.POST.get("Education_Level")
        Number_of_Dependents = request.POST.get("Number_of_Dependents")
        Years_of_Employment = request.POST.get("Years_of_Employment")
        Current_Debt = request.POST.get("Current_Debt")
        Credit_Utilization_Ratio = request.POST.get("Credit_Utilization_Ratio")
        
        completion = client.completions.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = f"""Loan Approval Prediction:
            Credit Score: {Credit_Score}
            Income: {Income}
            Debt-to-Income Ratio (DTI): {Debt_to_Income_Ratio}
            Employment Status: {Employment_Status}
            Loan Amount: {Loan_Amount}
            Loan Term: {Loan_Term}
            Credit Utilization Ratio: {Credit_Utilization_Ratio}
            Age: {Age}
            Purpose of Loan: {Loan_Purpose}
            Current Debt: {Current_Debt}
            Years of Employment: {Years_of_Employment}
            Number of Dependents: {Number_of_Dependents}
            Education Level: {Education_Level}
            Marital Status: {Marital_Status}
            Housing Status: {Housing_Status}
            Savings: {Savings}
            Assets: {Assets}
            Payment History: {Payment_History}
            Based on the provided information, please predict the likelihood (High  or Low ) that the applicant will avail the loan. one word reply only""",
            stream = False
        )
        time.sleep(5)
        context = {
            "ct": completion.choices[0].text
        }
        print(completion.choices[0].text)
        return render(request, 'loan_app/final.html', context)
    return render(request, 'loan_app/index.html')


def dbtinc(request):
    return render(request, 'loan_app/dbtinc.html')

def emi(request):
    return render(request, 'loan_app/emi.html')