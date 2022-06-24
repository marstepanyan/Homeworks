string = str(input('sentence : '))


def palindromes(data):
    return data == reverse_sentence(data)


def reverse_sentence(sentence):
    words = sentence.split(' ')
    rev_sentence = ' '.join(reversed(words))
    return rev_sentence


print(palindromes(string))  # information school graduate seeks graduate school information
