# Nested if program example

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is not positive.")
    if num == 0:
        print("It is zero.")
    else:
        print("It is negative.")