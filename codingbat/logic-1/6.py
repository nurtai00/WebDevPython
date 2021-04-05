def alarm(n, m):
    if m == True:
        if n == 0:
            return "off"
        else:
            return "10-00"
    elif m == False:
        if n == 0:
            return "10-00"
        else:
            return "7-00"