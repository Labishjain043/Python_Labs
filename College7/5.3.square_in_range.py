input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

squares_in_range = [x ** 2 if 10 <= x <= 20 else x for x in input_list]

print("Squares of numbers in the range 10-20 (unchanged for others):", squares_in_range)
