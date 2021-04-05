def hiapp(n):
    count = 0
    for i in range(len(n)):
        if n[i:i+2] == 'hi':
            count = count + 1
    return count

print(hiapp('hihihihih'))