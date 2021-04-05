x = input()
d = int(input())
cnt = int(0)

for i in x:
    if int(x) % 10 == d:
        cnt = cnt + 1
        x = int(x) // 10

print(cnt)