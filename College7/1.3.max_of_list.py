lst = list(input("Enter the list of integers separated by spaces: ").split())
largest_element = int(lst[0])

for i in lst:
    i = int(i)
    if i > largest_element:
        largest_element = i
print("Largest element:", largest_element)
