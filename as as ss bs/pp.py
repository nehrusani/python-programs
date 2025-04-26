"""
is it by writting the code we used isalpha and argv isalpha is just to write str and arvg is a collection of pythpon word thankyou
"""
import sys
papa = sys.argv[1]
papa2 = sys.argv[2]
if papa.isalpha() and papa2.isalpha():
    
    print(papa, papa2)
else:
    print("not possible")
