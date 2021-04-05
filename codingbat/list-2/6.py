def next2(n):
    for i in range(len(n)):
        if n[i] == 2 and n[i+1] == 2:
            return True
        else:
            return False

print(next2([2, 1, 2]))