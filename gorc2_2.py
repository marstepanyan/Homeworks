num = int(input('number : '))
res = []


def divider(n):
    return [i for i in range(1, n+1) if n % i == 0]


print(divider(num))
