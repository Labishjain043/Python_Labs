def replace_spaces_with_hyphens(input_str):
    hyphenated_str = ""
    for char in input_str:
        if char == ' ':
            hyphenated_str += '-'
        else:
            hyphenated_str += char
    return hyphenated_str


def to_snake_case(input_str):
    words = input_str.split('-')
    snake_case = '_'.join(words)
    return snake_case


def to_camel_case(input_str):
    words = input_str.split('-')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case


sentence = input("Enter a sentence: ")

hyphenated_sentence = replace_spaces_with_hyphens(sentence)
snake_case = to_snake_case(hyphenated_sentence)
camel_case = to_camel_case(hyphenated_sentence)

print("Hyphenated Sentence:", hyphenated_sentence)
print("Snake-case Format:", snake_case)
print("Camel-case Format:", camel_case)
