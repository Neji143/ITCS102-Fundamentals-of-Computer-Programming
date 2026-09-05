#USING OPERATORS

input("Welcome to the cashier! Press enter to continue...")

print()

total_price = eval(input("how much is your money? "))
total = total_price

print()

n = eval(input("Enter the price for the rice --> "))
total = total - n

e = eval(input("Enter the price for the eggs --> "))
total = total - e

i = eval(input("Enter the price for the milk --> "))
total = total - i

l = eval(input("Enter the price for the bread --> "))
total = total - l

d = eval(input("Enter the price of your discount coupon --> "))
total= total + d

print()

print("Your change is ---> ", total)
