lst = [1, 3, 0, 5, 1, 3, 7, 9]


def contain(data, val):
    i = 0
    while i < len(data):
        if data[i] == val:
            return True
        i += 1

    return False


contain_value = 3
print("list cotains", contain_value, ":", contain(lst, contain_value))


def pop(data, i=None):
    if i is None:
        del data[len(data) - 1]
        return data
    else:
        _value = data[i]
        del data[i]
        return _value


print(pop(lst, 4))


def remove_all(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(value)
        i += 1
    return data


print(remove_all(lst, 3))

lst1 = [4, 5, 3, 6, 17, 7, 8, 9]


def reverse(data):
    i = 0
    res = []
    while i < len(data):
        res.append(data[len(data) - 1 - i])
        i += 1
    return res


print(reverse(lst1))


def max(data):
    _max = data[0]
    i = 0
    while i < len(data):
        if data[i] >= _max:
            _max = data[i]
        i += 1
    return _max


print("maximum value in lst1:", max(lst1))


def min(data):
    _min = data[0]
    i = 0
    while i < len(data):
        if data[i] <= _min:
            _min = data[i]
        i += 1
    return _min


print("minimum value in lst1:", min(lst1))
