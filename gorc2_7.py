import random
lst1 = []
for i in range(1, 7):
    num = random.randint(1, 49)
    lst1.append(num)


def remove_duplicated(lst):
    res = []
    for item in lst:
        if item not in res:
            res.append(item)
    return res


print('my numbers : ', remove_duplicated(lst1))
print('in order : ', sorted(remove_duplicated(lst1)))
