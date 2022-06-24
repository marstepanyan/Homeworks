letter = str(input('letter from latin alphabet : '))


def vowels(let):
    if let in ('a', 'e', 'i', 'o', 'u'):
        return 'vowel letter'
    elif let == 'y':
        return 'both vowel and consonant'
    elif len(let) > 1:
        return 'that\'s not a letter'
    return 'consonant'


print(vowels(letter))
