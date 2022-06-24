import math


v0 = 0
a = 9.8
d = float(input('height : '))

v = math.sqrt((v0 ** 2) + (2 * a * d))


print('speed =', v)
