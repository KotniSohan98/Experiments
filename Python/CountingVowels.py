def minion_game(string):
    vowel="AEIOU"
    new=""
    count=0
    for item in string:
        if item in vowel and item not in new:
            new+=item
            print(item+" vowel")
            count+=string.count(item)

    print(count)
minion_game("AAAEEEIOSRV")