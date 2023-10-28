x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

if x < 0 or y < 0:
    print("Invalid input. Please enter non-negative integers.")
else:
    if y % x == 0:
        print(y, "is divisible by", x)
    else:
        print(y, "is not divisible by", x)
