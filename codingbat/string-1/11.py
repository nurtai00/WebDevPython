def rot(n):
    rotated = n[:2]
    aft = n[2:len(n)]
    return aft + rotated
print(rot('Temirlan'))