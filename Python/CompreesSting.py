def compressString(string):
    string1=""
    i=0
    len_str=len(string)
    while(i!=len_str):
        count=1
        while((i<(len_str-1)) and string[i]==string[i+1]):
            count=count+1
            i=i+1
        if count == 1:
            string1=string1+str(string[i])
        else:
            string1 =string1 + str(string[i])+str(count)
        i=i+1
    return string1
print(compressString("aabbbcdddd"))