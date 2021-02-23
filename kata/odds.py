# Solution by PauloBA

def odds(values):
    oddNums = []
    for i in values:
        if i % 2 == 1:
            oddNums.append(i)
    return oddNums