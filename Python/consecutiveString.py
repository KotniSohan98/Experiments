def consecutive(string):
    string1=""
    i=0
    len_str=len(string)
    flag=0
    while(i!=len_str):
        count=1
        while((i<(len_str-1)) and string[i]==string[i+1]):
            count=count+1
            i=i+1
        if count >= 4:
            print("Invalid")
            flag=1
            break
        i=i+1
        if count >=4:
            break
    if flag !=1:
        print("Valid")


consecutive("4424444424442444")
#consecutive("4123456789123456")
consecutive("5133336789123456")