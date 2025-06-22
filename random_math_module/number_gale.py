import random
player = True
number=str(random.randint(10,20))
print("i will generrate a number from 10 to 20 and you have to guess the number 1 digit at a time!!!")
print("the game ends when you get 1 hero!!!")
while player :
    guess = str(input("geus the number : "))
    if number == guess :
        print("you win the game👌👌")
        print(number)
        break
    else:
        print("lets  retry it again till you have the right guess!!!😁")