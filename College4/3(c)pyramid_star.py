n = int(input("Enter the number of rows for the pyramid: "))
row = 1

while row <= n:
    spaces = n - row
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * row - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    row += 1
