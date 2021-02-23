# Solution by PauloBA

def solution(string):
    word = []
    ac = ''
    for i in string: 
        word.append(i)
    word.reverse()
    for i in word:
        ac = ac + i
    return ac

arg = 'PauloBA'

print(solution(arg))