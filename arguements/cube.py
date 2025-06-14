def cube(num1):
    return num1 * num1 * num1
# define a function wich execute cube function to check if user enterd number is divisible by 3
def cubeby3(num1):
    if num1 % 3 == 0 :
        return cube(num1)
        print("number is divisible by three ")
    else:
        print("number is not / by 3")
print(cubeby3(9))
