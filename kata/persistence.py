# Solution by PauloBA

def persistence(n):
    n = str(n)
    tl = []
    acN = 1
    c = 0
    for i in n:
        tl.append(int(i))
    if len(tl) == 1:
        return 0
    for i in tl:
        acN = acN * i
    c = c + 1
    while acN > 9:
        tl = []
        for i in str(acN):
            tl.append(int(i))
        acN = 1
        for i in tl:
            acN = acN * i
        c = c + 1
    return c

print(persistence(39))