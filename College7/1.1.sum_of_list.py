lst = list(input("Enter the list of integers separated by spaces: ").split())
sm = 0

for i in lst:
    i = int(i)
    sm += i
print("Sum of elements:", sm)
