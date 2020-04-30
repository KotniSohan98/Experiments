def show(string):
    vowel="AEIOU"
    u1=set()
    u2=set()
    for i in range(len(string)):
        if string[i] in vowel:
            for j in range(len(string[i:])):
                print(string[i:i+j+1])
        else:
            for k in range(len(string[i:])):
                print(string[i:i+k+1])
show("BANANA")