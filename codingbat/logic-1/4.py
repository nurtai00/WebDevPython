def drive(n, m):
    if m == False:
        if n <= 60:
            return "0"
        elif n <= 80 and n >= 61:
            return "1"
        elif n >= 81:
            return "2"
    elif m == True:
        if n <= 65:
            return "0"
        elif n <= 85 and n >= 66:
            return "1"
        elif n >= 86:
            return "2"