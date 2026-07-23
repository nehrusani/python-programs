word = str(input("enter your word : "))
space = ""
for i in range(len(word)-1,-1,-1):
    space = space+word[i]
print("reversed ",space)


word = str(input("enter your word : "))  #laptop
word1 = ""
for i in range(len(word)-1,-1,-1): #
    word1 = word1+word[i]
print("after reverse",word1)