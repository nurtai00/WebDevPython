def closefar(a, b, c):
    if abs(a - b) <= 1 or abs(a - c )<= 1:
        if abs(a - b) >= 2 or abs(a - c) >= 2:
            return True
        else:
            return False
    else:
        return False

print(closefar(1, 2, 10))