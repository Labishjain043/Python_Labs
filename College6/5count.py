upper = 0
lower = 0
digit = 0
special = 0

sentence = input("Enter a sentence: ")

index = 0
while index < len(sentence):
    char = sentence[index]
    ascii_value = ord(char)
    if 65 <= ascii_value <= 90:
        upper += 1
    elif 97 <= ascii_value <= 122:
        lower += 1
    elif 48 <= ascii_value <= 57:
        digit += 1
    else:
        special += 1
    index += 1

print("Digits: ", digit)
print("Alphabets: ", upper + lower)
print("Special characters: ", special)
print("Capital letters: ", upper)
print("Small letters: ", lower)
