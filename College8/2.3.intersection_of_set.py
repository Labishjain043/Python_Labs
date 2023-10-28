list1 = [int(x) for x in input("Enter the first list of integers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers separated by spaces: ").split()]

intersection_of_sets = [x for x in list1 if x in list2]

print("Intersection without sets:", intersection_of_sets)
