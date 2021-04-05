def short(n, m):
    if len(n) < len(m):
        return n + m + n
    else:
        return m + n + m

print(short('Dastan', 'Timaasdasd'))