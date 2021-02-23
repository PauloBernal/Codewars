# Solution by PauloBA

def get_count(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    nV = 0
    for i in input_str:
        if i in vowels:
            nV = nV + 1
    return nV
