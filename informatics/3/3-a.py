a = input()
b = input()
c = int(2)

if a < b:
    for x in range(int(b)):
        if (c < int(b)):
            print(c)
            c = c + 2
        else:
            break
else:
    print('sorry, "a" is higher than "b"')