def xyz(a):
    for i in range(len(a)):
        if a[i] != '.' and a[i+1: i+4] == 'xyz':
            return True
    if a[i: i+3]:
        return True
    return False