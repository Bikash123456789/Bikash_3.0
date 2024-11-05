for i in range(1, 6):
    # Print Spaces
    for space in range(1, 6 - i):
        print(" ", end="")

    # Print Star
    for star in range(1, i + 1):
        print("*", end="")
    print()
