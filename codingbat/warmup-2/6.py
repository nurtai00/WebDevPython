def array_count(n):
    count = 0
    for i in n:
        if i == 9:
            count = count + 1
    return count

print(array_count([5, 8, 9, 5, 9, 7]))