n = int(input())
i = int(2)

while n > i:
    if n % i == int(0):
        break
    else:
        i = i + 1
print(i)