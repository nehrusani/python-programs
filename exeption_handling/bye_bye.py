valaid = False
while not valaid:  
    try:
        a = int(input("enter a number : "))
        while a %  2 == 0 :
            print("Bye")
        valaid = True
    except ValueError :
        print("invaild")