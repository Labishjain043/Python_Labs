Number = int(input("Enter a number: "))
s = 0
while Number != 0:
    digit = Number % 10
    s += digit
    Number //= 10

print("Sum is: ", s)
