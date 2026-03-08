"""hello childeren and parents this a safe cheker for your childeren
function used for it : __init__() and ohno()
use of __init__() function : this function is there for sending an argument and definig it
use of ohno() function : this function checks if your age is ok or not it has conditions
use of g :it is a var for storing each data
  """
print("are you fit for squid game???")
g = input("do you played or watch squid game? :\na. yes\nb. no\n")
if g == "a" or g == "a.":
    print("fine,lets check your age lest you are watching or playing it in a young age !!!please childeren donot play or watch this!!!")
    class checker :
        def __init__(self,age):
            self.age = age
        def ohno(self):
            if self.age <= 17:
                print("no you dont have right to play squid game!")
            else:
                print("you are okay for it but you should not play squid game")
    oi = checker(int(input("enter your age : ")))
    oi.ohno()
elif g == "b" or g == "b.":
    print("no checking is needed donot distrect")
else:
    print("you enterd invailed")
