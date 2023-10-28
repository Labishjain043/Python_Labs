def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
    return result


input_string = input("Enter a Sentence: ")
result = remove_duplicates(input_string)
print(result)
