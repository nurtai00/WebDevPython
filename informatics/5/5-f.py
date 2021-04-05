n = int(input())
i = int(0)
j = int(0)
nums = []
cnt = int(0)
while n > i:
    var = int(input())
    nums.append(var)
    i = i + 1
for s in range(0, n-1):
    if nums[j-1] < nums[j] and nums[j] > nums[j+1]:
        cnt = cnt + 1
    j = j + 1
print(cnt)