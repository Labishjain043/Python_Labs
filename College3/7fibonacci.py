N = int(input("Enter the number of terms in the Fibonacci sequence: "))

a, b = 1, 1

if N <= 0:
    print("Please enter a valid Input!")
elif N == 1:
    print("Fibonacci sequence (first term): 1")
else:
    count = 2
    print("Fibonacci sequence (first 2 terms): 1, 1")
    while count < N:
        next_term = a + b
        print(next_term, end=", ")
        a, b = b, next_term
        count += 1
