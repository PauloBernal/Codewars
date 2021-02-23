sm = [[1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]]

sm2 = [[1,  2,  3,  4],
       [12, 13, 14, 5],
       [11, 16, 15, 6],
       [10,  9,  8, 7]]

def snail(snail_map):
    ans = []
    c = 0
    nMtx = snail_map
    l = len(snail_map)
    for i in snail_map[0]:
        ans.append(i)
    for i in range(l):
        if i > 0 and i < l - 1:
            ans.append(snail_map[i][len(snail_map[i]) - 1])
    snail_map[-1].reverse()
    for i in snail_map[-1]:
        ans.append(i)
    snail_map.reverse()
    for i in range(l):
        if i > 0 and i < l - 1:
            ans.append(snail_map[i][0])
    for i in nMtx:
        for j in i:
            if j in ans:
                i.remove(j)
    nMtx.remove(nMtx[0])
    nMtx.remove(nMtx[l - 2])
    nMtx.reverse()
    for i in nMtx:
        for j in i:
            c = c + 1
    if c > 0:
        if c == 1:
            ans.append(nMtx[0][0])
        else:
            for i in nMtx[0]:
                ans.append(i)
            for i in range(len(nMtx)):
                if i > 0 and i < len(nMtx) - 1:
                    ans.append(nMtx[i][len(nMtx[i]) - 1])
            nMtx[-1].reverse()
            for i in nMtx[-1]:
                ans.append(i)
            nMtx.reverse()
            for i in range(len(nMtx)):
                if i > 0 and i < len(nMtx) - 1:
                    ans.append(nMtx[i][0])
            for i in nMtx:
                for j in i:
                    if j in ans:
                        i.remove(j)
        if len(nMtx) > 1:
            nMtx.remove(nMtx[0])
            nMtx.reverse()
        c = 0

    return ans

print(snail(sm))
print(snail(sm2))