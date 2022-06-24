import math


s1 = float(input('length of 1st side : '))
s2 = float(input('length of 2nd side : '))
s3 = float(input('length of 3rd side : '))

s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))


print('area of triangle =', area)
