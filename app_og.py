from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apply")
def apply():
    return render_template("apply.html")

@app.route("/submit_application", methods=["POST"])
def submit_application():
    # Retrieve form data

    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    AvailableBankcardCredit = float(request.form.get("availableBankCredit"))
    TotalInquiries = int(request.form.get("totalInquiries")) 
    AverageCreditScore = int(request.form.get("creditScore"))
    StatedMonthlyIncome = float(request.form.get("monthlyIncome"))
    MonthsOfEmployementExperience = int(request.form.get("workExperienceMonths"))
    IsHomeowner = int(request.form.get("homwOwner"))
    Term = int(request.form.get("loanTerm"))
    LoanAmount = float(request.form.get("loanAmount"))
    AnyDelinquencies = int(request.form.get("delinquencies"))
    OpenCreditLines = int(request.form.get("openCreditLines"))
    monthlyDebtPayment = float(request.form.get("monthlyDebtPayment"))
    DebtToIncomeRatio = float(monthlyDebtPayment/StatedMonthlyIncome)
    LoanPurpose = request.form.get("loanPurpose")
     
    if (request.form.get("loanPurpose")=="home"):
        InterestRate = 0.10
    elif(request.form.get("loanPurpose")=="auto"):
        InterestRate = 0.12
    elif(request.form.get("loanPurpose")=="education"):
        InterestRate = 0.15
    else:
        InterestRate = 0.09

    # Define loan parameters
    Principal = LoanAmount
    AnnualInterestRate = InterestRate
    LoanTermMonths = Term

    # Convert annual interest rate to monthly interest rate
    MonthlyInterestRate = AnnualInterestRate / 12 

    # Calculate monthly installment using the formula
    MonthlyInstallment = Principal * (MonthlyInterestRate * (1 + MonthlyInterestRate) ** LoanTermMonths) / ((1 + MonthlyInterestRate) ** LoanTermMonths - 1)

    print("Monthly Installment:", round(MonthlyInstallment, 2)) 
   
    data = [InterestRate, MonthlyInstallment, AverageCreditScore, Term, AnyDelinquencies,
            IsHomeowner, DebtToIncomeRatio, StatedMonthlyIncome, OpenCreditLines]
    
    final_features = [np.array(data)]
    prediction = model.predict(final_features)[0]

    if DebtToIncomeRatio >43:
        message = 'Debt to income too high! Unfortunately, your loan application was not approved.'
        prediction = 0
    elif StatedMonthlyIncome <= 1000:
        message= 'Monthly income too low! Unfortunately, your loan application was not approved.'
        prediction = 0
    elif AverageCreditScore <= 579:
        message = 'Poor credit score! Unfortunately, your loan application was not approved.'
        prediction = 0
    elif TotalInquiries >= 8:
        message = 'Too many Inquiries! Unfortunately, your loan application was not approved.'
        prediction = 0
    elif MonthsOfEmployementExperience < 12 and LoanPurpose != "education":
        message = 'Insufficient employement experience! Unfortunately, your loan application was not approved.'
        prediction = 0
    elif prediction == 0:
        message = 'Unfortunately, your loan application was not approved.'
    else:
        message = 'Congratulations! Your loan has been approved.'
    
    # Return a response 
    return render_template("result.html", first_name=first_name, prediction=prediction, monthly_installment=round(MonthlyInstallment, 2),message=message)

if __name__ == "__main__":
    app.run(debug=True)