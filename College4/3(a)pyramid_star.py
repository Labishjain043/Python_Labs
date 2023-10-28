n = int(input("Enter the number of rows for the pyramid: "))

row = 1

while row <= n:
    stars = row
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    row += 1
