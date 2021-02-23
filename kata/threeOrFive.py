# Solution by PauloBA

def solution(number):
    c = number - 1
    ac = 0
    nums = []
    while c > 0:
        if c % 3 == 0 or c % 5 == 0:
            nums.append(c)
        c = c - 1
    for i in nums:
        ac = ac + i
    print 
    return ac

print(solution(10))