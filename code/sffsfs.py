import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

score = 0
com_score = 0

while True:
    print("\n--- Current Score ---")
    print(f"User: {score} | Computer: {com_score}")
    print("First to 3 wins takes the match!\n")
    
    print("Enter your choice \n rock \n paper \n scissors \n")

    choice_name = input("Enter your choice: ").lower()

    while choice_name not in ["rock", "paper", "scissors"]:
        choice_name = input('Enter a valid choice please : ').lower()

    if choice_name == 'rock':
        choice = 1
    elif choice_name == 'paper':
        choice = 2
    else:
        choice = 3

    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = "draw"
    elif (choice == 2 and comp_choice == 1) or (choice == 1 and comp_choice == 2):
        result = 'paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'rock'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'scissors'

    if result == "draw":
        print("<== it's a tie! ==>")
    elif result == choice_name:
        print("<== user wins! ==>")
        score = score + 1
        print(score)
    else:
        print("<== computer wins! ==>")
        com_score = com_score + 1
        print(com_score)

    if com_score == 3:
        print("computer wins the match")
        break
    elif score == 3:
        print("user wins the match")
        break

print("Thanks for playing!")
