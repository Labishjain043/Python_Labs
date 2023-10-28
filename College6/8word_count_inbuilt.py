def count_word_in_sentence(sentence, word):
    word_count = sentence.count(word)
    contains_word = word in sentence

    return contains_word, word_count

sentence = input("Enter a Sentence: ")
word = input("Enter a Word: ")

contains_word, word_count = count_word_in_sentence(sentence, word)
print("Contains 'word':", contains_word)
print("Number of occurrences of 'Word':", word_count)
