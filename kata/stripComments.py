# Solution by PauloBA

import re

def solution(string, markers):
    ans = []
    dAns = ''
    pattern1 = re.compile(r'(.*)\n')
    pattern2 = re.compile(r'.*\n(.*)$')
    lines = []
    res1 = re.findall(pattern1, string)
    res2 = re.findall(pattern2, string)
    for i in res1:
        lines.append(i)
    for i in res2:
        lines.append(i)
    if len(markers) > 0:
        for line in lines:
            com = []
            for i in markers:
                try:
                    if line[0] == i:
                        com.append('')
                        break
                except:
                    pass
                pattern3 = re.compile(rf'(.*)\s(\{i}.*)')
                res = re.match(pattern3, line)
                if res:
                    com.append(res.group(1))
            com.sort(key = lambda ele: len(ele))
            if len(com) == 0:
                ans.append(line)
            else:
                ans.append(com[0])

        if len(ans) > 0:
            for i in range(len(ans) - 1): 
                dAns = dAns + ans[i] + '\n'
            dAns = dAns + ans[len(ans)-1]
        else:
            dAns = dAns
        print(lines)
        print(ans)
        return dAns
    else:
        return string

arg = "\n#hola"
mk = ["#"]

print(solution(arg, mk))