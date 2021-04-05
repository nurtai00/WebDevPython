def parrot(n, m):
    if n and m < 7 or m > 20:
        return True
    else:
        return False

print(parrot(False, 6))