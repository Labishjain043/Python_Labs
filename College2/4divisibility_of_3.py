def number(n):
    st = str(n)
    summ = 0

    for i in st:
        summ += int(i)

    if summ % 3 == 0:
        return "The number is divisible by 3!"
    else:
        return "The number is not divisible by 3!"


n = int(input("Write the number for checking its divisibility by 3: "))
print(number(n))
