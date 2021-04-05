def twostr(a, b):
    la = len(a)
    lb = len(b)
    if a == b[len(b) - la: len(b)] or b == a[len(a) - lb: len(a)]:
        return True
    else:
        return False

print(twostr('Hiabc', 'abc'))