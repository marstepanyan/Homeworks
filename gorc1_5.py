count1 = int(input('count of bottles under 1l : '))  # <=1l  $0.10
count2 = int(input('count of bottles over 1l : '))  # >1l    $0.25
total = "{:.2f}".format((count1 * 0.10) + (count2 * 0.25))


print('in total $', total)
