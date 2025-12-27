money = 12323
pay = int(input("enter the widrew amount : "))

if pay < 12323 :
    money -= pay
    print("your money has been withdrawn")
    while True:
        pay = int(input("enter the widrew amount : "))
        if pay == 0:
            break
        if pay < money:
            money -= pay
            print("your money has been withdrawn")
        else:
            print("you are not for so much money capable")
else:
  print("you are not for so much money capable")
