a = input()
b = input()

for x in range(int(a), int(b)):
    if int(x ** 0.5) ** 2 == x:
        print(x)