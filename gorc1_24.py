value = None
num = -1
sum_ = 0


while value != 0:
    value = int(input('number = '))
    sum_ += value
    num += 1
    if num == 0 and value == 0:
        raise ValueError


def arithmetic_mean(sum, count):
    mean = sum / count
    return mean


print(arithmetic_mean(sum_, num))
