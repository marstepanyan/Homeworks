def pascals_triangle(n, r):
    if n == 1 or r == 1 or r == n:
        return 1
    else:
        return pascals_triangle(n - 1, r) + pascals_triangle(n - 1, r - 1)


n = 4
r = 3
print("the number in", n, "row and", r, "column is: ", pascals_triangle(n, r))
