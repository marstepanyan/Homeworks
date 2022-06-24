d = int(input('days : '))
h = int(input('hours : '))
m = int(input('minutes : '))
s = int(input('seconds : '))

sec = (((((d * 24) + h) * 60) + m) * 60) + s


print('period in seconds =', sec)
