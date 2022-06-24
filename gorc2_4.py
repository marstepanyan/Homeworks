lst1 = [1, 3, 5, 7, 9]
lst2 = [22, 44, 66, 88, 100]


def zip(data1, data2):
    result = []
    for i in range(len(data1)):
        res = [data1[i], data2[i]]
        result.append(res)
    return result


print(zip(lst1, lst2))
