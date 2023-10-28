import math

epsilon = float(input("Enter Epsilon (ε): "))
x = float(input("Enter x: "))

n = 0  # Initialize n to 0
series = 0
i = 0

while True:
    factorial = math.factorial(2 * n)
    nth_term = ((-1) ** n) * (x ** (2 * n)) / factorial
    series += nth_term

    if abs(nth_term) < epsilon:
        break

    n += 1
    i += 1

print(series)
print(i)
