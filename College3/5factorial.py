N = int(input("Enter a positive integer: "))

if N < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    factorial = 1
    i = 1
    while i <= N:
        factorial *= i
        i += 1

    print("The factorial of", N, "is: ", factorial)
