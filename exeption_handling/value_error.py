try:
    number=int(input("enter a number : "))
    print(number)
except ValueError as a :
    print("exception :",a)
print("outside the exception")