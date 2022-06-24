year = int(input('year: '))
month = int(input('month: '))


def days_in_month(m, y):
    if m == 2 and y % 4 == 0:
        return 'has 29 days'
    elif m == 2 and y % 4 != 0:
        return 'has 28 days'
    elif m in (1, 3, 5, 6, 8, 10, 12):
        return 'has 31 days'
    elif m in (4, 7, 9, 11):
        return 'has 30 days'
    elif m < 1 or m > 12:
        return 'not a month'


print(days_in_month(month, year))
