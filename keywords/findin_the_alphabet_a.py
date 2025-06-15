text = str(input("enter any word : "))
for i in text:   
    if i == "A" or i == "a" :
        print("a is found! sucessfull!")
        break
    else:
        print("Error! a is not found in this word! Please type a word with a!")