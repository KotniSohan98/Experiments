def credit(s):
    format1 = "xxxx-xxxx-xxxx-xxxx"
    format2 = "xxxxxxxxxxxxxxxx"
    num = "1234567890"
    s1 = ""
    if s == "":
        return "Invalid"

    for j in s:
        if j in num:
            s1 += str("x")
        else:
            s1 += str("-")
    # print(s1)
    if s1 == format1 or s1 == format2:
        # print("no error")
        return first(s)
    else:
        return "Invalid"


def first(s):
    num1 = "456"
    s1 = s.replace("-", "")
    # s2 = s1.replace(" ", "")
    if s1[0] in num1:
        return consecutive(s1)
    else:
        return "Invalid"


def consecutive(inp_string):
    string1 = ""
    k = 0
    len_str = len(inp_string)
    flag = 0
    while k != len_str:
        count = 1
        while (k < (len_str - 1)) and inp_string[k] == inp_string[k + 1]:
            count = count + 1
            k = k + 1
        if count >= 4:
            return "Invalid"
            flag = 1
            break
        k = k + 1
        if count >= 4:
            break
    if flag != 1:
        return "Valid"


string = input()

for i in range(int(string)):
    string = input()
    print(credit(string))

# print(credit("4253625879615786"))
# print(credit("4424424424442444"))
# print(credit("5122-2368-7954-3214"))
#
# print(credit("42536258796157867"))
# print(credit("4424444224442444"))
# print(credit("5122-2368-7954 - 3214"))
# print(credit("44244x4424442444"))
# print(credit("0525362587961578"))
#
# print("----------------------------------------------")
# print(credit("3695-7963-915827-75"))
# print(credit("3143-4672-8798-2968-2968"))
# print(credit("6444-4444-4444-4918"))
# print(credit("6865396515642918"))
# print(credit("6865396515642"))
# print(credit("4695-7963-9778-2775"))