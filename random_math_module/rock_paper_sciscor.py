import random
while True :
    player = input("eneter the choice(rock,paper,scissor) : ")
    posible_action=["rock","paper","scissor"]
    computer_action=random.choice(posible_action)
    print(f"you chose {player},computer choice {computer_action}")
    if player == computer_action :
        print("both player selected the same choice its a tie!!!😮‍💨")
    elif player == "rock":
        if computer_action == "scissor":
            print("rock mashes the scissor you win!!!🏆🥇")
        else:
            print("paper covers rock you lose!!!")
    elif player == "paper":
        if computer_action == "rock":
            print("paper covers the rock you win!!!🏆🥇")
        else:
            print("scissor cuts paper you lose!!!")
    elif player == "scissor":
        if computer_action == "paper":
            print("scissor cuts the paper you win!!!🏆🥇")
        else:
            print("rock mashes the scissor you lose!!!😭")
    play = input("playagain yes or no :")
    if play == "no" : 
        break
    elif play == "yes" :
        continue
    else:
        print("invaild answer!!!")