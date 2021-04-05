n = int(input())
i = int(1)
while n > i:
    sqrt = i ** 0.5
    if (int(sqrt) ** 2) == i:
        print(i)
    i = i + 1