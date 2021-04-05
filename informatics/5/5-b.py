n = int(input())
i = int(0)
j = int(1)
nums = []
while n > i:
    var = int(input())
    nums.append(var)
    i = i + 1

while n > j:
    print(nums[j])
    j = j + 2