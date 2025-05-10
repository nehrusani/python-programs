x = input("Enter your first subject:")
x = input("Enter your second subject:")
if x == "English":
    print(x)
elif x == "Math":
    print (x)
    print("want to continue")
else:
    print("not acepted")
    while True:
        y = input("enter yes or no:")
        if y == "yes":
            print(y)
            if y == "no":
                break 

    