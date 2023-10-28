input_list = [int(x) for x in input("Enter a list of positive integers separated by spaces: ").split()]
unique_elements = []

for num in input_list:
    if num not in unique_elements:
        unique_elements.append(num)
print("List with duplicate elements removed (Method 1):", unique_elements)
