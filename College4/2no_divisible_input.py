N = int(input("Enter a positive number N: "))

if N <= 0:
    print("Please enter a positive number.")
else:
    print("Numbers not divisible by", N, "in the range 1-1000:")

    num = 1
    while num <= 1000:
        if num % N == 0:
            num += 1
            continue
        print(num, end="")
        num += 1
