print()
# TASK1
print()


loanamount = 1000
loanyears = 2
rate = 0.002506
remainingloan = loanamount
principal = loanamount / (loanyears * 12)
interest = remainingloan * rate
monthlypayment = interest + principal

print(f"TASK 1 \n \n Enter the loan amount: ${loanamount} \n Enter the loan period in years: {loanyears}")
print("\n Payment Schedule \n Month \t | \t Monthly Payment \t | \t Interest \t | \t Principal \t | \t Remaining Loan")
print("-" * 109)

for x in range(1, (12 * loanyears) + 1):
    interest = remainingloan * rate
    monthlypayment = interest + principal
    remainingloan = remainingloan - principal

    print(f"{x} \t | \t ${monthlypayment:.2f} \t\t | \t ${interest:.2f} \t\t | \t ${principal:.2f} \t\t | \t ${remainingloan:.2f}")
print()


print()
#TASK2
print()

print("TASK 2")
print()

for x in range(7):
    for y in range(13):
        if x == 6 or x + y == 6 or (x >= 1 and y - x == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
#TASK3
print()

print("TASK 3")
print()

for x in range(5):
    for y in range(5):
        if x == 0 or x == 4 or x + y == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()