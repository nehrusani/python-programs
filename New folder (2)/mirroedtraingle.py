totalrows=int(input("Enter the Number of Rows : "))
for row in range(totalrows):
    for space in range(totalrows-row-1):
        print(" ",end="")
    for symbol in range(row+1):
            print("*",end="")
    print()