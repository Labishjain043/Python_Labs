capital_count = 0
small_count = 0
digit_count = 0
special_count = 0

sentence = input("Enter a sentence: ")

index = 0
while index < len(sentence):
    char = sentence[index]
    ascii_value = ord(char)
    if 65 <= ascii_value <= 90:
        capital_count += 1
    elif 97 <= ascii_value <= 122:
        small_count += 1
    elif 48 <= ascii_value <= 57:
        digit_count += 1
    else:
        special_count += 1

    index += 1

print("Capital letters:", capital_count)
print("Small letters:", small_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
