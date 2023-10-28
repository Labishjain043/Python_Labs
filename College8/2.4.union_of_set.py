list1 = [int(x) for x in input("Enter the first list of integers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers separated by spaces: ").split()]

union_of_sets = list(list1 + [x for x in list2 if x not in list1])

print("Union without sets:", union_of_sets)
