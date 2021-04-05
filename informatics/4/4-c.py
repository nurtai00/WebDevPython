n = int(input())
i = int(0)

while n > i:
        sqrt = 2 ** i
        if sqrt > n:
            break
        else:
            print(sqrt)
            i = i + 1