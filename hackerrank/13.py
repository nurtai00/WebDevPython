numbers = input().strip().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
T = tuple(numbers)
print(hash(T))