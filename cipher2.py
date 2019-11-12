def convert_letter(letter, rotate_by=13):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # rotate_by is an optional argument
    position = alphabet.index(letter)
    new_position = (position + rotate_by) % 26
    new_letter = alphabet[new_position]

    return new_letter

def convert_sentence(sentence):
    new_sentence = ''
    for letter in sentence:
        new_sentence += convert_letter(letter)
    return new_sentence

print(convert_sentence('hello'))
# the_new_letter = convert_letter('a')
# print(the_new_letter)
