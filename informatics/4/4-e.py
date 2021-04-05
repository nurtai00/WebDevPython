n = int(input())
i = int(0)
while 1 < n:
    i = i + 1
    sqrt = 2 ** i
    if sqrt >= n:
        print(i)
        break