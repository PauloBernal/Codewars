def maskify(cc):
    if len(cc) <= 4:
        ans = ""
        for i in cc:
            ans = ans + i
    else:
        list = []
        for i in cc:
            list.append(i)

        ans = ""
        nLen = len(cc) - 4
        for i in range(len(list)):
            if i < nLen:
                ans = ans + "#"
            else:
                ans = ans + list[i]
    return ans    

print("Password: " + maskify("Hello"))

