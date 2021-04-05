x = input()
sum = int(0)
size = len(x)
for i in x:
    sum = sum + int(i) * (2 ** (size - 1))
    size = size - 1
print(sum)