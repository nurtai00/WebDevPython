def xor(a,b):
    res = int(0)
    if a == 0 and b == 0:
        res = 0 * 1 + 1 * 0
        print(res)
    if a == 0 and b == 1:
        res = 0 * 0 + 1 * 1
        print(res)
    if a == 1 and b == 0:
        res = 1 * 1 + 0 * 0
        print(res)
    if a == 1 and b == 1:
        res = 1 * 0 + 0 * 1
        print(res)
xor(0, 0)