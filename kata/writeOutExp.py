# Solution by PauloBA

def expression_out(exp):
    list = []
    sorter = []
    ans = ""
    ac = ""
    c = 0
    op = {'+':'Plus', '-':'Minus', '*':'Times', '/':'Divided By', '**':'To The Power Of', '=':'Equals', '!=':'Does Not Equal'}
    expressions = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', '+':'Plus', '-':'Minus', '*':'Times', '/':'Divided By', '**':'To The Power Of', '=':'Equals', '!=':'Does Not Equal', ' ':' '}
    for i in exp:
        list.append(i)
    for i in list:
        if i == " ":
            sorter.append(ac)
            sorter.append(" ")
            ac = ""
        else:
            ac = ac + i
    for i in sorter:
        if i == " ":
            c = c + 1
        else:
            if c > 0:
                if i not in op:
                    return "That's not an operator!"
    sorter.append(ac)
    print(sorter)
    for i in range(len(sorter) - 1):
        if i != " ":
            try:
                ans = ans + expressions[sorter[i]]
            except KeyError:
                return "That's not an operator!"
    ans = ans + expressions[sorter[-1]]
    return ans

print(expression_out('2 5 10'))