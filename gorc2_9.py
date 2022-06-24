def is_sublist(data1, data2):
    if not data2:
        return True
    elif data2 == data1:
        return True
    elif len(data2) > len(data1):
        return False
    else:
        for i in range(len(data1)):
            if data1[i] == data2[0]:
                n = 1
                while (n < len(data2)) and (data1[i + n] == data2[n]):
                    n += 1
                return n == len(data2)


larger = [1, 2, 3, 4]
smaller = [2, 4]

print(is_sublist(larger, smaller))
