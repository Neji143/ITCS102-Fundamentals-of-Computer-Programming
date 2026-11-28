for i in range(1,6):
    print("--" * (5 - i), end = "")

    for y in range(1, i + 1):
        print(y, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end = " ")

    print()