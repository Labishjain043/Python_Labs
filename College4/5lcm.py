def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calculate_lcm(a, b):
    return a * b // calculate_gcd(a, b)


N = int(input("Enter the number of positive integers: "))

if N <= 0:
    print("Please enter a positive integer for N.")
else:
    numbers = []

    for i in range(N):
        num = int(input(f"Enter positive integer {i+1}: "))
        if num <= 0:
            print("Please enter positive integers only.")
            break
        numbers.append(num)

    if len(numbers) == N:
        lcm = numbers[0]

        for i in range(1, N):
            lcm = calculate_lcm(lcm, numbers[i])

        print(f"The LCM of {', '.join(map(str, numbers))} is {lcm}.")
