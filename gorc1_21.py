month = str(input('name of month : '))


def days_of_month(name):
    if name == 'feb':
        return '28 or 29'
    elif name in ('jun', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'):
        return '31'
    elif name in ('apr', 'jun', 'sep', 'nov'):
        return '30'
    else:
        return 'there is no month with such a name'


print(days_of_month(month))
