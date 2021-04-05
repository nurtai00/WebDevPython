def lasttwo(n):
    size = len(n)
    if size < 2:
        return "incorrect"
    return n[size-2:] * 3
print(lasttwo('Nurtay'))