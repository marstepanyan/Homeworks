word = str(input('word: '))
w_lst = []

for idx in range(len(word)):
    w_lst = w_lst + [word[idx]]


def rev_word(data):
    i = 0
    res = []
    while i < len(data):
        res = res + [data[len(data) - 1 - i]]
        i += 1
    return res


def joined(lst):
    w_str = ''
    for i in range(len(lst)):
        w_str += lst[i]
    return w_str


print('reversed word:', joined(rev_word(word)))
