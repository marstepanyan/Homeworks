def sum_of_squares(a, b, c):
    if a <= b and a <= c:
        return b ** 2 + c ** 2
    elif a >= b and c >= b:
        return a ** 2 + c ** 2
    else:
        return a ** 2 + b ** 2


num1 = 4
num2 = 2
num3 = 5
print("sum of squares = ", sum_of_squares(num1, num2, num3))
