# Solution by PauloBA

def max_multiple(divisor, bound):
    c = bound
    ans = 0
    while c > 0 and ans == 0:
        if c % divisor == 0:
            ans = c
        c = c - 1
    return ans

print(max_multiple(3, 26))