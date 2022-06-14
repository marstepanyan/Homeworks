def pow(base, exp):
    if exp > 0:
        return base ** exp
    elif exp < 0:
        return 1 / base ** (-exp)
    else:
        return 1


a = 2
b = -2
print(a, "raised to power of", b, "=", pow(a, b))
