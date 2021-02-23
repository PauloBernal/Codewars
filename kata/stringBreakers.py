def string_breakers(n, st):
    nSt = ""
    c = 0
    ac = ""
    pieces = []
    ans = ""
    for letter in st:
        if letter != " ":
            nSt = nSt + letter
    for i in nSt:
        if c < n:
            ac = ac + i
            c = c + 1
        else:
            pieces.append(ac)
            ac = i
            c = 1
    for i in pieces:
        ans = ans + i + "\n"
    ans = ans + ac
    return ans

print(string_breakers(5, "Hello It Is Me Who You Were Looking For"))
