def sum(a, b):
    res = 0
    while a <= b:
        res += a
        a += 1
    return res


print("sum from a to b = ", sum(2, 5))
