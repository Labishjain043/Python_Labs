sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_sentence = ' '.join(reversed(words))

print("Original sentence:", sentence)
print("Reversed sentence:", reversed_sentence)
