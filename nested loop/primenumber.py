firstnumber = int(input("Ebetr the upper range : "))
secondnumber = int(input("Enter the lower range : "))
for a in range(firstnumber,secondnumber):
    if a>0:
        for i in range(2,a):
            if (a % i) == 0 :
                break
        else:
            print(a,"it is a prime number!")