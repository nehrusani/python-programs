"""
we made a calculater
we used to store in the file 
we also used output.
"""
while True:
    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    choicey = input("choose + - * /: ")
    if choicey == "+":
        output = x  +  y
        print(output)
    if choicey == "-":
        output = x - y
        print(output)
    if  choicey == "*":
        output = x * y
        print(output)
    if  choicey == "/":
        output = x / y
        print(output)    