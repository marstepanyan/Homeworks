def get_median(data):
    data.sort()
    print('sorted list:', data)
    n = len(data)
    m = n // 2
    if n % 2 == 0:
        median = (data[m - 1] + data[m]) / 2
        return median
    return data[m]


lst = [3, 13, 2, 10, 34, 11, 26, 47]
print('median:', get_median(lst))
