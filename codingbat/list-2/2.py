def bigdif(a):
    for i in range(len(a)-1):
        maximum = max(a)
        minimum = min(a)
    return maximum - minimum

print(bigdif([10, 3, 5, 6]))