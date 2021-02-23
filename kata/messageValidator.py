def is_a_valid_message(message):
    ans = ""
    words = []
    lens = []
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    acword = ""
    num = ""
    if message == "":
        ans = True
    else:
        for char in message:
            if char in nums:
                if acword != "":
                    words.append(acword)
                num = num + char
                acword = ""
            else:

                if num != "":
                    lens.append(int(num))
                    num = ""
                acword = acword + char

        words.append(acword)
        if len(words) != len(lens):
            ans = False
        else:
            for i in range(len(words)):
                if len(words[i]) == lens[i]:
                    ans = True
                else:
                    ans = False
                    break

    return ans
    print(words)
    print(lens)


print(is_a_valid_message("4code13hellocodewars"))
print(is_a_valid_message("3hey5hello2hi5"))