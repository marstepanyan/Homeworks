number = int(input('number : '))


def perfect_number(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num


print(perfect_number(number))
