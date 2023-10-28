X = int(input("Enter the lower limit: "))
Y = int(input("Enter the Upper limit: "))
N = int(input("Enter the number whose multiples between the above two numbers are to be printed: "))

i = X + 1
if X < Y:
    while i <= Y:
        if i % N == 0 and X <= Y:
            print(i)
        i += 1
else:
    print("Please Enter a Valid Input!")
