class pair_elemets :
    def towsum(self,num,target):
        Lookup = {}
        for i,n in enumerate(num):
            if target-n in Lookup :
                return (Lookup[target-n],i)
value = int(input("eneter sum of wich you want to macke your sarch " ))
print(f"index1 = {pair_elemets().towsum((10,20,30,40,50,60,70),value)}")