def prime(m):
    i = 2
    while i <= m // 2:
        if m % i == 0:
            return False
        else:
            i += 1
    return True


def smallest_prime(n):
    if prime(n + 1):
        return n + 1
    return smallest_prime(n + 1)


num = 7
print('smallest prime number greater than', num, ':', smallest_prime(num))
