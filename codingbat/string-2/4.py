  
def cntcode(n):
    cnt = 0
    for i in range(0,len(n) - 3):
        if n[i:i+2] == 'co' and n[i+3] == 'e':
            cnt = cnt + 1

    return cnt