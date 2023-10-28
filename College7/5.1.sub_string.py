input_list = input("Enter a list of strings separated by spaces: ").split()
sample_string = input("Enter the sample string to search for: ")

count = sum([1 for s in input_list if sample_string in s])

print("Number of strings containing the sample string:", count)
