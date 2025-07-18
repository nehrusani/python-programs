while True:
    try:
        number = int(input("enter a number: "))
        if number > 34:
            print("swalow time")
        elif number < 34:
            print("to small i wnat more!")
        else:
            print("no decimals or string pleas retry")
    except ValueError:
        print("Invalid input, please enter an integer.")

    ask = input("do you want to retry : ").strip().lower()
    if ask != "yes":
        break
