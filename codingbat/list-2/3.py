def maxmin(a):
    sum = 0
    for i in a:
        sum = sum + i
    return (sum - max(a) - min(a))/ (len(a)-2)