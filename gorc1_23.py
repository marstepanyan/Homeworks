month = str(input('month : '))
day = int(input('day : '))


def season(m, d):
    if (m in ('apr', 'jun', 'sep', 'nov') and d > 30) \
            or (m in ('jun', 'mar', 'may', 'jul', 'aug', 'oct', 'dec') and d > 31) \
            or (m == 'feb' and d > 29):
        return 'wrong day'
    elif m in ('dec', 'jan', 'feb'):
        return 'winter'
    elif m in ('mar', 'apr', 'may'):
        return 'spring'
    elif m in ('jun', 'jul', 'aug'):
        return 'summer'
    elif m in ('sep', 'oct', 'nov'):
        return 'autumn'
    return 'wrong month'


print(season(month, day))
