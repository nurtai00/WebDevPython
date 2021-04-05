def nearhund(n):
    if 100 - n <= 10 or 200 - n <= 10:
        return True
    else:
        return False

print(nearhund(89))