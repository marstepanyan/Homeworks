def is_even(n):
    return n % 2 == 0


def even_idx(data):
    res = []
    for i in range(len(data)):
        if is_even(data[i]):
            res.append(i)
    return res


lst = [3, 6, 8, 9, 11, 24, 13]
print('index of even items:', even_idx(lst))
