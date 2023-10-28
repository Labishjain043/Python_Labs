lst = list(input("Enter the list of integers separated by spaces: ").split())
product = 1

for i in lst:
    i = int(i)
    product *= i
print("Product of elements:", product)
