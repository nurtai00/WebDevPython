n = int(input())
i = int(0)
cnt = int(0)
nums = []
while n > i:
    var = int(input())
    nums.append(var)
    if nums[i] >= 0:
        cnt = cnt + 1
    i = i + 1
print(cnt)