val_lst = []

while True:
    value = input('enter a number: ')
    if value == '':
        break
    else:
        val_lst.append(int(value))


def arithmetic_mean(val, count):
    return val / count


def less_than_mean(func, val):
    return [i for i in val if i < func]


def more_than_mean(func, val):
    return [i for i in val if i > func]


def equal_to_mean(func, val):
    return [i for i in val if i == func]


print('mean: ', arithmetic_mean(sum(val_lst), len(val_lst)))
print('less than mean: ', less_than_mean(arithmetic_mean(sum(val_lst), len(val_lst)), val_lst))
print('more than mean: ', more_than_mean(arithmetic_mean(sum(val_lst), len(val_lst)), val_lst))
print('equal to mean: ', equal_to_mean(arithmetic_mean(sum(val_lst), len(val_lst)), val_lst))
