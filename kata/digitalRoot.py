# Solution by PauloBA

def digital_root(n):
    n = str(n)
    ls = []
    ans = 0
    for i in n:
        ls.append(int(i))
    for i in ls:
        ans = ans + i
    if ans < 10:
        return ans
    else:
        return digital_root(ans)

print(digital_root(24))