N = int(input("Enter the number of lines (N): "))

if N <= 0:
    print("Please enter a positive integer for N.")
else:
    i = 1
    while i <= N:
        j = N
        while j > i:
            print(" ", end=" ")
            j -= 1

        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1

        j = i - 1
        while j > 0:
            print("*", end=" ")
            j -= 1

        print()
        i += 1
