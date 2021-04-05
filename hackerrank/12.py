def wrap(st, n):
    for i in range(0, len(st), n):
        res = st[i:i+n]
        if len(res) == n:
            print(res)
        else:
            return(res)

wrap("abadcadcadasd", 3)