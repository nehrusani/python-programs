rows = int(input("enter a amount of number : "))
for i in range(1,rows + 1):
    print(" "*(rows - i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(rows-1,0,-1):
    print(" "*(rows - i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()