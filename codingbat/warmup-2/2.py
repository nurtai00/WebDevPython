def timess(n, m):
    if len(n) <= 3:
        return n * m
    else:
        return n[0:3] * m
print(timess('Chocolate', 8))