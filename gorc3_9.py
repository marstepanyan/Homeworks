import random


def random_passwd(n):
    pwd = []
    for i in range(n + 1):
        pwd.append(chr(random.randint(33, 126)))
    return pwd


print('passwd:', random_passwd(4))
