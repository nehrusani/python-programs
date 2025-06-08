x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = input("Enter an operator (+, -, *, /): ")
if z == "+":
    print(f"{x} + {y} = {x + y}")
elif z == "-":
    print(f"{x} - {y} = {x - y}")
elif z == "*":
    print(f"{x} * {y} = {x * y}")
elif z == "/" :
    print(f"{x} / {y} = {x / y}")
else:
    print("invailed operater")        