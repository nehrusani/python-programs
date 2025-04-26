"""
#  Interactive program to ask and print result accordingly

x=input("enter a color ")
if x == "gree":   
   print("good")
elif x == "black":
   print("ok")
else:   
   print("bad")
   """

import sys
x = sys.argv 
if x == "green":
    print("good")
else:
    print("bad")    
