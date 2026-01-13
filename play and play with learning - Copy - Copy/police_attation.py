ui = str(input("which problem do you have : "))
uiu = str(input())
uiz =str(input())
if ui == "blackmailing":
    print("ok")
    print("during that time were you at home?")
    if uiu == "no" :
        print("ok so ai wich spot did you get a call ")
        if uiz == "market":
             print("what was the market name")
        
    elif uiu == "yes":
        print("Can we have your phone")
        if uiz == "no":
             print("sorry we can not help you")
        elif uiz == "yes":
             print("ok i am checking")
             print()
    else :
          print("invaidld input")
