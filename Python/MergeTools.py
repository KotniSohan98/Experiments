def merge_the_tools(string, k):
    n=len(string)
    num=int(n/k)
    string_1=""
    string_split=[string[i:i+num] for i in range(0, len(string), num)]
    print(string_split)
    for item in string_split:
        for i in item:
            if i not in string_1:
                string_1+=i
        print(string_1)
        string_1=""

#merge_the_tools("AABCAAADA",3)
merge_the_tools("ABCABHFHBHGFCVXD",4)