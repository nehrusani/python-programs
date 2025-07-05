
def visi(words):
    ctr = 0
    lst = []
    for i in words :
        if len(i)>1 and i[0]==i[-1]:
            ctr+=1
            lst.append(i)
    print("list of words with the first and last character same",lst)
    return ctr
count = visi(["apple","kiwi","appla","kiwk","eye"])
print("number of words having first and last character same",count)