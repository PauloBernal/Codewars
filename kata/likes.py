# Solution by PauloBA

def likes(names):
    ans = ""
    if len(names) == 0:
        ans = "no one likes this"
    elif len(names) == 1:
        ans = names[0] + " likes this"
    elif len(names) == 2:
        ans = names[0] + " and " + names[1] + " like this"
    elif len(names)==3:
        ans = names[0] +", "+names[1]+" and "+names[2]+" like this"
    else:
        ans = names[0] +", "+names[1] +" and "+str(len(names)-2) + " others like this"
    return ans