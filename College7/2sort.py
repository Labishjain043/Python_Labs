sorted_list = []
input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

for num in input_list:
    inserted = False
    for i in range(len(sorted_list)):
        if num < sorted_list[i]:
            sorted_list.insert(i, num)
            inserted = True
            break
    if not inserted:
        sorted_list.append(num)

print("Sorted List:", sorted_list)
