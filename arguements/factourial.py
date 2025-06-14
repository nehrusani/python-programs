def facrorial(n):
   if n == 0 or n == 1:
      return 1
   else :
      return n * facrorial(n - 1)
print("the factorial of 0 : " ,facrorial(0))
print("the factorial of 1 : " ,facrorial(1))
print("the factorial of 2 : " ,facrorial(2))
print("the factorial of 3 : " ,facrorial(3))
print("the factorial of 4 : " ,facrorial(4))
print("the factorial of 5 : " ,facrorial(5))