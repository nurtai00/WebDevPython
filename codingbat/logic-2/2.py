def summ(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b and a != c and b != c:
        return c
    elif a != b and a == c and b != c:
        return b
    elif a != b and a != c and b == c:
        return a
    elif a == b == c:
        return '0'

print(summ(2, 2, 2))