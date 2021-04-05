def counter(n, m):
    count = 0
    for i in range(len(n)):
        if n[i:].startswith(m):
            count += 1
    print(count)

counter('mamamsita','a')