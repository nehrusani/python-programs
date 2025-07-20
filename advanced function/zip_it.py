goo= {2,4,5,67,8 }
ops = {"hallo","Danke","Rot"}
momo = list(zip(goo,ops))
print(momo)
lo = [1,5,6,4,4,3,4]
go = [2,4,3,5,3,4]
for x,y in zip(lo,go[::-1]):
    print(x,y)
mydict = {ops:goo for ops,goo in zip(ops,goo)}
print(mydict)