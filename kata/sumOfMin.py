# Solution by PauloBA

def sum_of_minimums(numbers):
    ans = 0
    for i in numbers:
        i.sort()
        ans = ans + i[0]
    return ans