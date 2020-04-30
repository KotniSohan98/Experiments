def street(list):
    count1=0
    for item in list:
        count=item[1]-item[0]
        count1+=count

    return count1
print(street([[5,8],[10,12]]))