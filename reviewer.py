age = int(input("AGE: "))
monthly_revenue = float(input("ENTER MONTHLY REVENUE: "))
cc = int  (input("ENTER CREDIT SCORE: "))
years_in_business = float(input("ENTER YEARS IN BUSINESS: "))
has_defaults = bool(input("HAS DEFAULTS? (Yes/No): ")) == "Yes"
collateral_name = input("ENTER COLLATERAL NAME: ")
collateral_value = float(input("ENTER COLLATERAL VALUE: "))

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("Business Loan Application Approved: Meets basic requirements.")

    max_loan_limit = 0
    base_processing_fee = 0
    if cc >= 720:
        max_loan_limit = 3 * monthly_revenue
        print("MAX LOAN LIMIT: $", max_loan_limit)
        if monthly_revenue >= 50000:
            base_processing_fee = 0.015 * max_loan_limit
            print("BASE PROCESSING FEE: $", base_processing_fee)
        else:
            base_processing_fee = 0.025 * max_loan_limit
            print("BASE PROCESSING FEE: $", base_processing_fee)
            if collateral_value >= max_loan_limit:
                print("Collateral Approved: ", collateral_name)
            else:
                print("Insufficient collateral value for", collateral_name)
                surcharge = max_loan_limit * base_processing_fee
                if collateral_value % 5000 != 0:
                    surcharge += 250
                    print("Surcharge for insufficient collateral: $250")
                    print("Your total processing fee is: $", surcharge)
                else:
                    print("No surcharge for collateral value divisible by 5000")

    elif 620 <= cc < 720:
        max_loan_limit = 1.5 * monthly_revenue
        print("MAX LOAN LIMIT: $", max_loan_limit)
        if years_in_business >= 5.0:
            base_processing_fee = 0.02 * max_loan_limit
            print("BASE PROCESSING FEE: $", base_processing_fee)
        else:
            base_processing_fee = 0.035 * max_loan_limit
            print("BASE PROCESSING FEE: $", base_processing_fee)
            if collateral_value >= max_loan_limit:
                print("Collateral Approved: ", collateral_name)
            else:
                print("Insufficient collateral value for", collateral_name)
                surcharge = max_loan_limit * base_processing_fee
                if collateral_value % 5000 != 0:
                    surcharge += 250
                    print("Surcharge for insufficient collateral: $250")
                    print("Your total processing fee is: $", surcharge)
                else:
                    print("No surcharge for collateral value divisible by 5000")

    elif cc < 620:
        print("Rejected: Credit score below requirement")
    else:
        print("Rejected: Does not meet basic requirements.")
else:
    print("Rejected: High Risk Application or Ineligible Owner")