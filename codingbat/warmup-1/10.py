def mischair(n, m):
    start = n[:m]
    end = n[m+1:]
    return start + end
print(mischair('kitchen', 5))