def reverce(r):
    e = len(r)-1
    s = 0
    while s < e :
        if (r[s]!=r[e]):
            return False
        s = s+1 
        e = e-1
    return True
r = ("e","y","e")
if reverce(r):
    print("tuple is flip flop")
else :
    print("the tuple is not flip flop")
