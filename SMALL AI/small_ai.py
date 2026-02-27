"""this code provides you infos if your age is okay for roblox hug me game each function has a meaning:
moonball():i used this function to keep some extra statements
__init__():i used this function to define the arguments given in the __int__
function
arguments: the arguments used in the game is there for defing the personal info
class(hug_me): provides you the information given to the user like your age 
secure data : this data cannot be sended to any social web and also not on and web search , app
where the data is going :the programm writen is reading the data and giving an output
extra : do not enter your real name due to data privacy!!!"""

class hug_me :
    def __init__(self,cartoon_character,your_age,your_name,your_year):
        self.cartoon_character = cartoon_character
        self.your_age = your_age
        self.your_name = your_name
        self.your_year = your_year
    def moonball(self):
        if self.your_age >= 18 :
            print("you can play this game")
        else:
            print("you cannot play this game")
            breakpoint()
        if self.your_year <= 2008 :
            print("you can play it ahead")
        else :
            print("no no no !!!!")
            breakpoint()
hug = hug_me(str(input("enter your favourite carrtoon character : ")),int(input("enter your age : ")),str(input("enter your name : ")),int(input("enter your birthyear : ")))
hug.moonball()