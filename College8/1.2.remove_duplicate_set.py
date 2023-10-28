input_list = [int(x) for x in input("Enter a list of positive integers separated by spaces: ").split()]
unique_set = [x for i, x in enumerate(input_list) if x not in input_list[:i]]

print("Set with duplicate elements removed:", unique_set)
