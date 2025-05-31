rows = int(input("enter your choice of number : "))
number = 1
for i in range(rows) :
    for j in range(i+1):
        print(number,end=' ')
        number = number + 1
    print()