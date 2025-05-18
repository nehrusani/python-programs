print("select your ride")
print("1.car")
print("2.bike")
choice = input("enter your choice : ")
if choice == "car":
    print("pleas select the type of car")
    print("1.Honda")
    print("2.Mercedenc benz")
    choice2 = input("enter your chioce : ")
    if choice2 == "Honda":
        print("you haveselected Honda")
    else:
        print("Mercedenz Benz")
elif choice == "Bike" :
    print("select the type of bike")
    print("1.Track")
    print("2.Haro") 
    choice3 = input("enter your choice : ")
    if choice3 == "Track" :
        print("you have selected Track")
    else:
        print("you have seleted Haro")
else:
    print("wrong input!")        