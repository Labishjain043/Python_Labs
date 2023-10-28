sentence = input()
sentence = sentence.lower()
vowel = 0
consonant = 0
word = 0

for i in sentence:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel += 1
    elif i == ' ':
        word += 1
    else:
        consonant += 1
print(vowel)
print(word + 1)
print(consonant)
