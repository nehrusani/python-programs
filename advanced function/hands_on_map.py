mylist = [1,4,5,7,9,4,3]
mylist2 = [2,4,5,6,4,5,4]
result = map(lambda x,y : x + y,mylist,mylist2)
print(list(result))
def func(l):
    return l*l
square = list(map(func,mylist))
print(square)