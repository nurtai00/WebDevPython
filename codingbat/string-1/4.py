def makeword(n, m):
    size = len(n)
    front = n[:size-2]
    end = n[size-2:]
    return front + m + end
print(makeword('<<>>', 'Dastan'))