n = int(input("Enter the number of terms whose 'Sum' is to be calculated: "))

series = 0
nat_num = 1
factorial = 1

for i in range(n):
    formula = 1/factorial
    nat_num += 1
    factorial *= nat_num
    series += formula
print(f'{series:.9f}')
