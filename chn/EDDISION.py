print("improve you sceince")
print("do you want to login in ?")
u = str(input())

if u == "yes" or u == "Yes":
    print("enter your email")
    z = str(input())
    if z == "nina@.gemail-.com":
        print("enter you mobile number")
        u = (input())
        if u == "+49 91918340" :
            print("enter your age")
            p = int(input())
            if p < 6 :
                print("you are to young to learn these things")
                breakpoint()
            else :
                print("what do you want to do "
                      "\n a.play quiz"
                      "\n read the story of sceintist then play quiz"
                      "\n log out")