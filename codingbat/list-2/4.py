def unlucky13(n):
    sum = 0;
    for i in n:
        if i != 13:
            sum = sum + i
        if i == 13:
            break
    return sum
print(unlucky13([1, 2, 2, 1, 13, 15]))