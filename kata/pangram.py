#Solution by PauloBA

#import string

def is_pangram(s):
    oL = []
    for i in s:
        j = i.lower()
        if j not in oL and j.isalpha():
            oL.append(j)
    if len(oL) == 26:
        return True
    else:
        return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))