route = [ "Terminal" ,"Perez Park", "Pacific Mall"]
passenger = []
seats = 6
Fare = 13
total = 0

while True:
    print()
    print("Sakay, ", passenger)
    print(len(passenger), "of" , seats, "seats.")
    print("===============================")
    print("\n1. Sakay\n2. Priority Seat\n3. Para Po!\n4. Baba Sa Pinto\n5. Baba Sa Harap\n6. Seat Check \n7. Reverse Route\n8. Exit")
    print("\n===============================")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(passenger) == seats:
             print("Sorry, puno na.")
           
        else:
            name = input("Enter your name: ")
            passenger.append(name)
            total += Fare
            print(name, "Took the priority seat")

    elif choice == 2:
        if len(passenger) == seats:
            print("Sorry, puno na.")
        else:
            name = input("Enter your name: ")
            passenger.insert(0, name)
            total += Fare
            print(name, "Took the priority seat")

    elif choice == 3:
        name = input("who is getting off? ")
        if name in passenger:
            passenger.remove(name)
            print(name, "has gotten off.")
        else:
            print(name, "is not on the jeep")

    elif choice == 4:
        if len(passenger) == 0:
            print("Walang pasahero sa jeep")
        else:
            left = passenger.pop(0)
            print(left, "has gotten off the door.")

    elif choice == 5:
        if len(passenger) == 0:
            print("Walang pasahero sa jeep")
        else:
            right = passenger.pop()
            print(right, "has gotten off the front door.")

    elif choice == 6:
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger[i])

    elif choice == 7:
        route.reverse()
        print("Route reversed:", route)

    elif choice == 8:
        print("Total fare collected: $", total)
        break

    else:
        print("Invalid choice. Please try again.")
