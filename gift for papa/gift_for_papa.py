import random
import time

def welcome():
    print("🎁 Welcome to the 'Gift for Papa' Game! 🎁")
    print("Papa loves surprises! Can you guess what gift he wants today?")
    print("You have 5 tries to guess the correct gift.\n")

def get_gift_list():
    return [
        "watch", "book", "wallet", "perfume", "tie",
        "chocolate", "pen", "mug", "shirt", "photo frame"
    ]

def play_game():
    gifts = get_gift_list()
    secret_gift = random.choice(gifts)
    attempts = 5

    print("Possible gifts:", ', '.join(gifts))
    for i in range(attempts):
        guess = input(f"Attempt {i+1}: What gift do you choose for Papa? ").strip().lower()
        if guess == secret_gift:
            print("🎉 Congratulations! Papa loves your gift! 🎉")
            break
        else:
            print("Hmm, Papa appreciates it, but that's not his favorite today.")
    else:
        print(f"Papa's favorite gift today was: {secret_gift}. Better luck next time!")

def main():
    welcome()
    play_game()
    print("\nThank you for playing! Give Papa a real hug today! 🤗")

if __name__ == "__main__":
    main()