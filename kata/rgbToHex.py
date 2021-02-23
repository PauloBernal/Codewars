# Solution by PauloBA

def toHex(color):
    hexChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if color <= 0:
        return '00'
    elif color >= 255:
        return 'FF'
    else:
        return f'{hexChar[((color)//16)]}{hexChar[((color)%16)]}'

def rgb(r, g, b):
    nr = toHex(r)
    ng = toHex(g)
    nb = toHex(b)
    return f'{nr}{ng}{nb}'


c1 = 16
c2 = 3
c3 = 254

print(rgb(c1, c2, c3))