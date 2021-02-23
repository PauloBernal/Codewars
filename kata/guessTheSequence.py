# Solution by PauloBA

def sequence(x):
    res = []
    n = (x//10)
    for i in range(n):
        res.append(i+1)
        d = (i+1)*10
        for j in range(10):
            if d+j <= x:
                res.append(d+j)
    for i in range(9):
        if i+1 not in res and i+1 <= x:
            res.append(i + 1)
    return res


print(sequence(8))