def credit(string):
    no="456"
    i=0
    string1=string.replace("-"," ")
    string2=string1.replace(" ","")
    print(string)
    print(string1)
    print(string2)
    len_str = len(string2)
    flag = 0
    if string2[0] in no and len(string2)==16:
        while (i != len_str):
            count = 1
            while ((i < (len_str - 1)) and string[i] == string[i + 1]):
                count = count + 1
                i = i + 1
            if count >= 4:
                print("Invalid")
                flag = 1
                break
            i = i + 1
            if count >= 4:
                break
        if flag != 1:
            print("Valid")
    else:
        print("Invalid")


#credit("4424444424442444")
#credit("4123456789123456")
#credit("4123-4567-8912-3456")
#credit("4123456789123456")
#credit("5123-4567-8912-3456")
#credit("61234-567-8912-3456")
#credit("4123356789123456")
credit("5133-3367-8912-3456")
#credit("5123 - 3567 - 8912 - 3456")