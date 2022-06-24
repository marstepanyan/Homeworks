fee = float(input('fee : '))


print('total :', "{:.2f}".format(fee))
print('tip :', "{:.2f}".format(fee * 18 / 100))
print('taxes :', "{:.2f}".format(fee * 20 / 100))
