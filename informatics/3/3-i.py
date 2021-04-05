  
x = input()
cnt = int(0)
for i in range(int(x), 1, -1):
    if int(x) % i == 0:
        cnt = cnt + 1
print(cnt)