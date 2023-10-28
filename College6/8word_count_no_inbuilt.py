def count_word_in_sentence_manual(sentence, word):
    word_count = 0
    contains_word = False
    sentence_length = len(sentence)
    word_length = len(word)

    for i in range(sentence_length - word_length + 1):
        if sentence[i:i + word_length] == word:
            word_count += 1
            contains_word = True

    return contains_word, word_count

# Example usage:
sentence = input("Enter a Sentence: ")
word = input("Enter a Word: ")

contains_word, word_count = count_word_in_sentence_manual(sentence, word)
print("Contains 'Word':", contains_word)
print("Number of occurrences of 'Word':", word_count)