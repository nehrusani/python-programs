import random
value = 2
Ditya = 0
player = True
number=str(random.randint(10,20))
print("i will generrate a number from 10 to 20 and you have to guess the number 1 digit at a time!!!")
print("the game ends when you get 1 hero!!!")
while player :
    guess = str(input("geus the number : "))
    Ditya = Ditya + 1
    print("Value of Ditya is: ", Ditya)
    if number == guess :
        print("you win the game👌👌")
        print(number)
        break
    if Ditya == 3:
        print("limitt exeeded") 
        break
    print("Computer generated random value is:  ", number)