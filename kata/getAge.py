# Solution by PauloBA

def get_age(age):
    n = ""
    for i in age:
        if i.isdigit():
            n = n + i
    ans = int(n)
    return ans