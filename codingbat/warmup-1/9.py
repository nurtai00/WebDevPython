def notstr(n):
    if len(n) >= 3 and n[:3] == "not":
        return n
    return "not " + n

print(notstr('candy'))