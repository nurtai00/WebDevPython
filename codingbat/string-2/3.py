def catdog(n):
    if cat(n) == dog(n):
        return True
    else:
        return False

def cat(a):
    cnt = 0
    for i in range(len(a)):
        if a[i:i+3] == 'cat':
            cnt = cnt + 1
    return cnt

def dog(a):
    cnt = 0
    for i in range(len(a)):
        if a[i:i+3] == 'dog':
            cnt = cnt + 1
    return cnt

print(catdog('catcatdog'))