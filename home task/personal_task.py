""" 
Datatyp must be integer what ever digit i give write tables as user give input    
"""

number=int(input("give any number : "))
x=str(input("do you want to continue : "))
while True:
   
    if x == "yes":
        for i in range(1,10) :
            logo=number*i
            print(logo)
        print(number)
    else:
        break

    