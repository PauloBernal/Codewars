# Solution by PauloBA

def spin_words(sentence):
    nLs = sentence.split(sep = " ")
    tLs = []
    for el in range(len(nLs)):
        i = nLs[el]
        print(i)
        if len(i) < 5:
            pass
        else:
            if len(i) >= 5:
                for j in i:
                    tLs.append(j)
            tLs.reverse()
            nLs[el] = "".join(tLs)
            tLs = []
    return " ".join(nLs)
print(spin_words("Hello my World"))