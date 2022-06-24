num = int(input('number : '))


def rev_num(a):
    m = 0
    while a != 0:
        n = a % 10
        m = m * 10 + n
        a = a // 10
    return m


print('reversed number:', rev_num(num))
