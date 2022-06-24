import math


r = float(input('radius : '))
h = float(input('height : '))

area = (math.pi * r)**2
volume = area * h


print('volume of cylinder =', "{:.1f}".format(volume))
