def fast_row(m, n):
    count = 1
    if n == 0:
        return 1
    if is_even(n):
        while count < n / 2:
            m *= m
            count += 1
        return m ** 2
    else:
        while count < (n - 1) / 2:
            m *= m
            count += 1
        return m * m ** 2


def is_even(n):
    return n % 2 == 0


m = 2
n = 3
print(m, "raised to power of", n, "=", fast_row(m, n))
