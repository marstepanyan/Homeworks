#1

lst1 = [3, 5, 7, 9, 13, 17]


def triple_item(item):
    return item * 3


def triple(func, data):
    res = [None] * len(data)
    for i in range(len(res)):
        res[i] = func(data[i])
    return res


print(triple(triple_item, lst1))



#2

def sum(a, b, c):
    return a + b + c


def map3(func, data1, data2, data3):
    res = [None] * len(data1)
    for i in range(len(res)):
        res[i] = func(data1[i], data2[i], data3[i])
    return res


print(map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))



#3

base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def pow(base, exp):
    return base ** exp


def map2(func, data1, data2):
    res = [None] * len(data1)
    for i in range(len(res)):
        res[i] = func(data1[i], data2[i])
    return res


print(map2(pow, base, exp))
