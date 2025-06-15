number = int(input("enter a number : "))
if (number % 20) == 0 :
    print("twist")
elif (number % 15) == 0 :
    pass
elif (number % 5) == 0 :
    print("fizz")
elif (number % 3) == 0 :
    print("buzz")
else:
    print(number)