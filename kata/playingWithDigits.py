# Solution by PauloBA

def dig_pow(n, p):
    dig = []
    w = str(n)
    d = 0
    for i in w:
        dig.append(int(i))
    for j in dig:
        d = d + j**p
        p = p + 1
    if d % n == 0:
        num = d/n
        return int(num)
    else: 
        return -1

print(dig_pow(46288, 3))