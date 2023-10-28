list1 = [int(x) for x in input("Enter the first list of integers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers separated by spaces: ").split()]

set_A = set(list1)
set_B = set(list2)

union_result = set_A.union(set_B)
intersection_result = set_A.intersection(set_B)
difference_A_B = set_A.difference(set_B)
difference_B_A = set_B.difference(set_A)
symmetric_difference = difference_A_B.union(difference_B_A)

print("Union of Set A and Set B:", union_result)
print("Intersection of Set A and Set B:", intersection_result)
print("Set Difference (A-B):", difference_A_B)
print("Symmetric Set Difference:", symmetric_difference)
