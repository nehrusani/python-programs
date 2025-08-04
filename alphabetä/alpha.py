# this will olny exept alphabet and if you write somthing else then int then it will say please enter a alpha
while True:
    x = input("enter a alpha : ")
    if x.isalpha():
        print("You entered a valid alphabetic string.")
    else:
        print("Please enter only alphabetic characters.")
    g = input("do you want to continue  : ")
    if g.lower() == "no":
        break