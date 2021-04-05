def posneg(n, m, z):
    if n > 0 and m < 0 or n < 0 and m > 0:
        return True
    elif z == True:
        if n < 0 and m < 0:
            return True
        else:
            return False
print(posneg(-1, -7, True))