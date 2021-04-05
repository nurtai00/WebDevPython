def diff(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

print(diff(100))