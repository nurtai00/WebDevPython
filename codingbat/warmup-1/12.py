def front3(n):
    if len(n) <= 3:
        return n * 3
    else:
        return n[0:3] * 3
print(front3('Chocolate'))