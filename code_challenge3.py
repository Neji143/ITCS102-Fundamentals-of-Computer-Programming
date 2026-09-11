#IF ELSE ELIF CODECHALLENGE 3

name = input("SENDERS NAME: ")
item = input("ITEM: ")

fragile = input("FRAGILE?: (yes/no): ")    
isit_fragile = fragile == "yes"

weight = float(input("WEIGHT: (in kg): "))
distance = float(input("DISTANCE WILL BE COVERED?: (in km): "))

express = input("IS EXPRESS? (yes/no): ")
isit_express = express == "yes"

international = input("IS INTERNATIONAL? (yes/no): ")
isit_international = international == "yes"

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not isit_express and not isit_international:
    total = 0.00
elif isit_international and isit_express:
    total = (base_cost * 1.40) + 50.00
elif isit_express or (isit_international and weight > 20.0):
    total = (base_cost * 1.20) + 25.00
elif weight > 30.0 or distance > 1000.0:
    total = base_cost + 30.00
else:
    total = base_cost

print("total cost: ", total, " PHP")

print("\n===================================")
print("\t\t\b\bRECEIPT")
print("===================================")
print("Sender Name:", name)
print("Item Type:", item)
print("Fragile:", isit_fragile)
print("-----------------------------------")
print("Weight:", weight, " kg")
print("Distance:", distance, " km")
print("Express:", isit_express)
print("International: ", isit_international)
print("===================================")
print("total cost: ", total, " PHP")
print("===================================")
