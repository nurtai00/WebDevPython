def date(n, m):
    if n >= 8 or m >= 8:
        return "2"
    elif n <= 2 or m <= 2:
        return "0"
    else:
        return "1"