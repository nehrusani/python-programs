while True:
    x = input("enter an alphabet : ")
    if x == "d":
        print("you lose the challange.")
    else:
        print("you are winnig.")
    y = input("do you want to continue : ")
    if y.lower() != "yes":
        break