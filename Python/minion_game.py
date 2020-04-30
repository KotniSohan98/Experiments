def minionGame(string):
    vowel="AEIOU"
    count1=0
    count2=0
    for i in range(len(string)):
        if string[i] not in vowel:
            count1+=len(string[i:]) #len(string)-i
        else:
            count2+=len(string[i:])  #len(string)-i
    if count1>count2:
        print("STUART",count1)
    elif count2>count1:
        print("KEVIN",count2)
    else:
        print("DRAW")
minionGame("BANANA")