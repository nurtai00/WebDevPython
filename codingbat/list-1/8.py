def maxi(n):
     m = max(n[0], n[1], n[2])
     n[0], n[1], n[2] = m
     return n[0] + n[1] + n[2]