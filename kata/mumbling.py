# Solution by PauloBA

def accum(s):
    l = len(s)
    chars = []
    nChars = []
    tem = ""
    for i in s:
        nChars.append(i.lower())
    for i in range(l):
        for j in range(i + 1):
            chars.append(nChars[i])
        chars.append("-")
    chars.pop()
    chars[0] = chars[0].upper()
    tem = chars[0]
    for i in range(len(chars)):
        if tem == "-":
            print(chars[i].upper())
            chars[i] = chars[i].upper()
            tem = chars[i]
        else:
            tem = chars[i]
    ans = "".join(chars)
    return ans

print(accum("abcdef"))

