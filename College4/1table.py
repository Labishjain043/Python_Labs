N = int(input("Write a Positive Integer: "))

i = 1
if N > 0:
    while i <= 20:
        print(N, "x", i, "=", N * i)
        i += 1
else:
    print("Enter a Valid Input!")
