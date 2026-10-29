#code challenge 6 ni neill

size = int(input("ENTER A NUMBER: -->"))

for x in range(size):
    for y in range(size):
        if x == y or x + y == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
