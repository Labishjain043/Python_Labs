n = int(input("Enter the number of terms whose 'Sum' is to be calculated: "))
x = int(input("Enter x: "))

series = 0
nat_num = 1

for i in range(n-1):
    formula = (x**nat_num)/nat_num
    nat_num += 1
    series += formula
series += 1
print(f'{series:.9f}')
