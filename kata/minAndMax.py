# Solution by PauloBA

def high_and_low(numbers):
    ls = numbers.split(sep=" ")
    nLs = []
    ans = ""
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    ls.sort()
    nLs.append(str(ls[-1]))
    nLs.append(str(ls[0]))
    ans = " ".join(nLs)
    return ans

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))