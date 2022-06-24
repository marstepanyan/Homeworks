def same_parity(n, *args):
    res = []
    for arg in args:
        if arg % n == 0:
            res.append(arg)
    return res


print('args that divide:', same_parity(3, 2, 6, 9, 7, 12, 5))
