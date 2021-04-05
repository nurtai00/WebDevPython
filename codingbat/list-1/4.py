def twoar(n, m):
    if n[0] ==  m[0] or n[-1] == m[-1] and len(n) > 1 and len(m) > 1:
        return True
    else:
        return False