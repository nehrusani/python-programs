totalrows=int(input("Enter the Number of Rows : "))
for row in range(1,totalrows+1):
    for space in range(1,(totalrows-row)+ 1):
        print(" ",end="")
        for symbol in range(1,row+1):
            print(" *",end=" ")
    print()