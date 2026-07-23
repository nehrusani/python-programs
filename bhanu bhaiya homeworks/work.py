"""money = int(input)
pincode =int(input("enter you safe code :"))
againcheck =int(input("enter your safe code : "))
if pincode == againcheck :
    print("move ahead")
else :
    print("you are not the person")
    quit()
enter = int(input("enter you enter amount till 200 euro : "))
if enter >= 200 :
    print("no money")
    quit()
take = int(input("enter you widrew amount : "))
if take <= 8999 :
    print("you have ",money-take,"balance in you account")
elif take >= 9001 :
    print("you are poor so-rry")
    quit()
elif take >= 9000 :
    print("sorrrry no morrre balance ")
else :
    quit()"""

balance = int(input("enter your balance : "))
ads     = str(input("do you want to plus minus : "))


amout   = int(input("amount :  "))
if ads == "+":
    pin     = int(input("enter : "))
    pin1    = int(input("enter : "))
    if pin == pin1 :
        print("your balance is ",balance+amout)
elif ads == "-":
    pin     = int(input("enter : "))
    pin1    = int(input("enter : "))
    if pin == pin1 :
        print("your balance is ",balance-amout)
