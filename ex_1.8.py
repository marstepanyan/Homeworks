def cube_root(n):
    root = 1
    while not close_enough(root, n):
        root = improve(root, n)
    return root


def close_enough(value, target):
    if abs(value ** 3 - target) < 0.0001:
        return True
    else:
        return False


def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) / 3


num = 7
print("cube root of", num, "=", cube_root(num))
