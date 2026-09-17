#code challenge 4 ni neillderosas
#sir check nyo nalang po huhuh mejo nalilito lang po ako dun sa bagong binigay nyong conditions huhuhud

import getpass

input("PRESS ENTER TO CREATE ACCOUNT:")
new_username = input("Enter new username: ")
new_password = input("Enter new password: ")
print("Account created successfully.")
print()

input("PRESS ENTER TO LOGIN:")
username = input("Username: ")
password = getpass.getpass("Password: ")

if username == new_username and password == new_password:
    print("Login successful!")
    print()

    input("PRESS ENTER TO EVALUATE LOAN:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    is_employed = bool(input("Is employed? (yes/no): ") == "yes")
    credit_score = int(input("Enter credit score: "))
    annual_income = float(input("Enter annual income: "))
    loan_amount = float(input("Enter amount to loan: "))
    has_collateral = bool(input("Has collateral? (yes/no): ") == "yes")

    what_collateral = "None"
    value = 0.0

    if has_collateral:
        what_collateral = input("Enter collateral description (ex. house, car, jewelry): ")
        value = float(input("Enter value of the collateral: "))
        
        if value < 30000:
            print("Invalid collateral value: Must be at least 30,000 PHP.")
            has_collateral = False  

    status = "REJECTED"
    reason = ""
    base_rate = 5.0  
    interest_rate = 0.0

    if 21 <= age <= 65 and is_employed:
        if credit_score >= 750: 
            if annual_income >= 100000:
                interest_rate = base_rate - 0.5
            else:
                interest_rate = base_rate
            status = "APPROVED"
            print("APPROVED at interest rate of", interest_rate, "%")

        elif 600 <= credit_score < 750:
            if has_collateral:
                interest_rate = base_rate + 2.0
            elif annual_income < 40000:
                interest_rate = base_rate + 4.5
            else:
                interest_rate = base_rate + 3.0
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

    print()
    print("===================================")
    print("\tLOAN EVALUATION SUMMARY      ")
    print("===================================")
    print(" Applicant Name  :", name)
    print(" Age             :", str(age))
    print(" Employment      :", "Yes" if is_employed else "No")
    print(" Credit Score    :", str(credit_score))
    print(" Annual Income   : PHP" + str(annual_income))
    print(" Loan Amount     : PHP" + str(loan_amount))
    print(" Collateral      :", "Yes (" + what_collateral + ")" if has_collateral else "Invalid collateral value: Must be at least 30,000 PHP.")
    if has_collateral:
        print(" Collateral Value: PHP" + str(value))
    print("-----------------------------------")
    print(" STATUS          :", status)

    if status == "APPROVED":
        print(" BASE RATE       :", str(base_rate) + "%")
        print(" INTEREST RATE   :", str(interest_rate) + "%")
    else:
        print(" REASON          :", reason)
    print("===================================")

else:
    print("Login failed. wrong username or password.")

