def sum(a, b):
    res = 0
    if a == b:
        return a
    elif a < b:
        while a <= b:
            res += a
            a += 1
        return res
    else:
        a, b = b, a
        while a <= b:
            res += a
            a += 1
        return res


a = 5
b = 2
print("sum from a to b = ", sum(a, b))
