def chlet(n):
    if len(n) <= 1:
        return n
    else:
        m = n[1:len(n)-1]
        return n[len(n)-1] + m + n[0]
print(chlet('code'))