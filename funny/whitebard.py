import random

def start_game():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("Can you guess what it is?")
    
    number = random.randint(1, 20)
    tries = 0

    while True:
        try:
            guess = int(input("👉 Your guess: "))
            tries += 1

            if guess < number:
                print("🔼 Too low! Try again.")
            elif guess > number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎊 You got it! The number was {number}.")
                print(f"👏 Great job! You guessed it in {tries} tries.")
                break
        except ValueError:
            print("⚠️ Please type a number!")

def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes":
            start_game()
        elif again == "no":
            print("👋 Thanks for playing! See you next time!")
            break
        else:
            print("Please type 'yes' or 'no'.")

if __name__ == "__main__":
    start_game()
    play_again()