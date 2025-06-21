try:
    num1 = int(input("write a number : "))
    num2 = int(input("wrire second number : "))
    result =num1 / num2
    print(result)
except ValueError as a :
    print("please enter a integer value!!!")
except ZeroDivisionError :
    print("the number is divided by zero!!!")
except SyntaxError :
    print("you forgot to eneter a number!!!")
except:
    print("wrong input")
else: 
    print("no exception")
finally:
    print("this will execute no matter what!!!")