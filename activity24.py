from activity23 import factorial
from activity23 import greet_me
from activity23 import box


while True:
    print("Select an option \n")
    print("1 - Factorial")
    print("2 - Greet Me")
    print("3 - Box")
    print("4 - Exit")
    choose = input("\nChoose an option: ")

    if choose == "1":
        print("FACTORIAL")
        num = int(input("Input any number: "))
        print(factorial(num))
        continue

    elif choose == "2":
        print("GREET ME")
        name = input("Enter any name: ")
        print(greet_me(name))
        continue

    elif choose == "3":
        print("BOX")
        size = int(input("Enter the size of box: "))
        print(box(size))
        continue

    elif choose == "4":
        print("System Exit")
        break

    else:
        print("invalid choice")
        continue