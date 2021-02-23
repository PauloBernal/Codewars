# Solution 1 by PauloBA

import re
pattern = re.compile(rf'(\(.*\))')
pattern2 = re.compile(rf'[\w]+(\))')
pattern3 = re.compile(rf'.*\([\w]+$')

def valid_parentheses(string):
    print(string)
    res = re.findall(pattern, string)
    res2 = re.match(pattern2, string)
    res3 = re.match(pattern3, string)
    print(pattern2)
    print(res2)
    a = 0
    b = 0
    state = True
    try:
        if string[0] == ')' or string[len(string) - 1] == '(':
            return False
    except:
        pass
    if res:
        for i in res[0]:
            if b > a:
                return False
            if i == '(':
                a = a + 1
                state = False
            elif i == ')':
                b = b + 1
                state = True
    else:
        for i in string:
            if i == '(':
                a = a + 1
            elif i == ')':
                b = b + 1
    if a == b:
        if res2 or res3:
            return False
        else:
            return state
    else:
        return False

# Solution 2 by PauloBA

def valid_parentheses(string):
    a = 0
    b = 0
    closed = True
    for i in string:
        if b > a:
            return False
        if i == '(':
            closed = False
            a = a + 1
        elif i == ')':
            closed = True
            b = b + 1
    if b == a:
        return closed
    else:
        return False

arg = 'ala((())()()))('

print(valid_parentheses(arg))