num = 5


def func_recursive(n):
    if n < 3:
        return n
    else:
        return func_recursive(n - 1) + func_recursive(n - 2) + func_recursive(n - 3)


print("when n =", num, "the number is :", func_recursive(num))


def func_interative(n):
    num0 = 0
    num1 = 1
    num2 = 2
    if n < 3:
        return n
    else:
        while n > 0:
            num0 = num0 + num1 + num2
            num0, num1, num2 = num1, num2, num0
            n -= 1
        return num0


print("when n =", num, "the number is :", func_interative(num))


def func(n, a=0, b=1, c=2):
    if n < 3:
        return c
    else:
        return func(n - 1, b, c, a + b + c)


print("when n =", num, "the number is :", func(num))
