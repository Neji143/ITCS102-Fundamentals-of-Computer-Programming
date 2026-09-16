#activity13 ni neill

name = input("Enter name: ")
age = int(input("Enter age: "))
is_employed = bool(input("Is employed? (yes/no): ") == "yes")
credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))
has_collateral = bool(input("Has collateral? (yes/no): ") == "yes")


status = "REJECTED"
reason = ""
interest_rate = 0.0

if age >= 21 and is_employed:
    if credit_score >= 750:  
        if annual_income >= 100000:
            interest_rate = 4.5
        else:
            interest_rate = 5.0
        status = "APPROVED"
        print("APPROVED at interest rate of", interest_rate, "%")

    elif 600 <= credit_score < 750: 
        if has_collateral:
            interest_rate = 7.0
        elif annual_income < 40000:
            interest_rate = 9.5
        else:
            interest_rate = 8.0
        status = "APPROVED"
        print("APPROVED at interest rate of", interest_rate, "%")

    else: 
        reason = "Credit score too low"
        status = "REJECTED"
        print("REJECTED: Credit score too low")

else:
    reason = "Fails baseline criteria"
    status = "REJECTED"
    print("REJECTED: Fails baseline criteria")

print("\n===================================")
print("      LOAN EVALUATION SUMMARY      ")
print("===================================")
print(" Applicant Name  :", name)
print(" Age             :", str(age))
print(" Employment      :", "Yes" if is_employed else "No")
print(" Credit Score    :", str(credit_score))
print(" Annual Income   : PHP" + str(annual_income))
print(" Collateral      :", "Yes" if has_collateral else "No")
print("-----------------------------------")
print(" STATUS          :", status)

if status == "APPROVED":
    print(" INTEREST RATE   :", str(interest_rate) + "%")
else:
    print(" REASON          :", reason)
print("===================================")