def choco(a, b, c):
    mb = c / 5

    if b >= mb:
        if a >= (c - mb * 5):
            return c + mb + 5
    if b <= mb:
        if a >= (c - b * 5):
            return c - b * 5
    return -1