input_string = input("Enter a hyphen-separated sequence of words: ")
word_list = input_string.split('-')

n = len(word_list)
for i in range(n):
    for j in range(0, n-i-1):
        if word_list[j] > word_list[j+1]:
            word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
sorted_string = '-'.join(word_list)
print("Sorted Result:", sorted_string)
