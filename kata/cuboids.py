# Solution by PauloBA

def find_difference(a, b):
    vA = 1
    vB = 1
    for i in a:
        vA = vA * i
    for i in b:
        vB = vB * i
    ans = abs(vA -vB)
    return ans