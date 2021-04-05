def oneten(n, m):
    if m == False:
        if 1 <= n <= 10:
            return True
        else:
            return False
    elif m == True:
        if n <= 1 or n >= 10:
            return True
        else:
            return False