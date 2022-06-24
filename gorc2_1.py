w = None
words = []
while w != '':
    w = input('word : ')
    words.append(w)
words.pop(-1)


def remove_duplicated(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


print(remove_duplicated(words))
