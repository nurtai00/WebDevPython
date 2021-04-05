n = int(input())
i = int(0)
sp = []
while i < n:
    x = input()
    sp.append(x)
    i = i + 1
sp.sort()
print(sp[n - 2])