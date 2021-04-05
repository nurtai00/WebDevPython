x = input()
y = 0

for i in x:
    z = int(x) % 10
    x = int(x) // 10
    y = y * 10
    y = y + z   

print(y)