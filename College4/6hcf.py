def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


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
        gcd = numbers[0]
        for i in range(1, N):
            gcd = calculate_gcd(gcd, numbers[i])

        print(f"The GCD of {', '.join(map(str, numbers))} is {gcd}.")
