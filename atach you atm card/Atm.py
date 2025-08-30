print("you have a balance of 3000rs")
money= 3000
get = int(input("enter how much you want to widrew : "))
password = int(input("enter you card number : "))
lessmoney=money-get
if money < get:
    print("you have to less balance in your card")
elif money > get:
    print("you have enough balance payment sucessfull !!!")
    print(f"there are in you account now rs. {lessmoney}")
