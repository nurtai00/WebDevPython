def noteen(a, b, c):
    return fixt(a) + fixt(b) + fixt(c)


def fixt(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

print(noteen(10, 13, 15))