mylist = [1,2,3,4,5,4,1,2,0]
count = 0
for i in mylist:
    count+=i
avr = count / len(mylist)
print("sum = ",count)
print(avr)    
mylist.sort()
print(mylist)
print(mylist[0])
print(mylist[-1])