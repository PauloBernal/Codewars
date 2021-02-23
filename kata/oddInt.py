# Solution by PauloBA

def find_it(seq):
    seq.sort()
    list = []
    sizes = []
    h = seq[0]
    c = 0
    for i in seq:
        if i not in list:
            list.append(i)
    for i in seq:
        if i == h:
            c = c + 1
        else:
            sizes.append(c)
            h = i
            c = 1
    sizes.append(c)
    for i in range(len(sizes)):
        if sizes[i] % 2 != 0:
            return list[i]
    

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))