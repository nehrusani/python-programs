tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
mine = len(tup1)<len(tup2)
length = len(tup1)
if len(tup2) < length:
    length = len(tup2)
for i in range(length):
    print(tup1[i], tup2[i])
for x in tup1:
    for i in tup2:
    y=x*i
    print(y)