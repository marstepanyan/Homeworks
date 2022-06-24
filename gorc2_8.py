value = None
val_lst = []

while value != 0:
    value = int(input('number = '))
    val_lst.append(value)

val_lst.pop(-1)


def ordered_list(lst):
    lst1 = sorted(lst)
    lst2 = sorted(lst, reverse=True)
    return lst == lst1 or lst == lst2


print(ordered_list(val_lst))
