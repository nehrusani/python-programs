# this for understanding
x = input("enter your name : ")
if x.isalpha() :
    print(x)
else:
    print("not a str")


y = input("enter your phone number :")

if y.isdigit():
    print(y)
else:
    print("not a number")
# is to understand the forloop
fruits = ["apple", "banana","ham"]
for a in fruits[:2]:
  print(a) 
