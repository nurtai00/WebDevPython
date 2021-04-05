def sortsum(n, m):
    if sum(n, m) >= 10 or sum(n, m) <= 19:
        return 20
    else:
        return sum(n, m)