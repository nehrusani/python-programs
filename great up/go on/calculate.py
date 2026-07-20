num = int(input("enter a num : "))
num2 = int(input("enter a num : "))
opo = str(input("enter an oporation : "))
if opo == "+":
    print(num + num2)
elif opo == "-":
    if num >= num2 :
        print(num - num2)
    else:
        print(num2 -num) 
elif opo == "*" :
    print(num * num2)
elif opo == "/" :
    if num >= num2 :
        print(num /num2)
    else :
        print(num2 / num)
else :
    print("invailed")