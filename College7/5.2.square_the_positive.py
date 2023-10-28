input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

squares = [x ** 2 if x > 0 else 0 for x in input_list]

print("Squares of positive integers (0 for non-positive):", squares)
