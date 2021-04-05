def mini(a, b, c, d):
    k = int(99999)
    if a < k:
        k = a
    if b < k:
        k = b
    if c < k:
        k = c
    if d < k:
        k = d
    print(k)

mini(5, 20, 3, 4)