word = str(input("write your own word : "))
charecter = str(input("Enter your own charector in this word : "))
i = 0
count = 0
while (i < len(word)) :
    if word[i] == charecter :
        count = count + 1
    i = i + 1
print("the total numbers of times" ,charecter,"has occured" ,count)