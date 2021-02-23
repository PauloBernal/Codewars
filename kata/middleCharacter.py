# Solution by PauloBA

def get_middle(s):
    ans = ""
    ls = []
    for i in s:
        ls.append(i)
    l = len(ls)
    if len(ls) == 0:
        return ans
    if len(ls) % 2 == 0:
        ans = ls[int(l/2) - 1] + ls[int(l/2)]
    else:
        ans = ls[int(l/2 - 0.5)]
    return ans