import string
def is_pangram(input_string):
    alphabet = set(string.ascii_lowercase)
    clean_string = ''.join(char.lower() for char in input_string if char.isalpha())
    return set(clean_string) == alphabet

input_string = input("Enter a Sentence: ")
result = is_pangram(input_string)

if result:
    print("The input string is a pangram.")
else:
    print("The input string is not a pangram.")
