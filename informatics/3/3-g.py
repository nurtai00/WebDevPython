x = input()
y = int(2)
for i in x:
    if int(x) % y != 0:
        y += 1
print(y)