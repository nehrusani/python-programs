import random

def we_must_be_nice():
    messages = [
        "🌟 We must be nice to everyone. 🌟",
        "Kindness is a gift everyone can afford to give.",
        "A simple smile or a helping hand can change someone's day.",
        "Let's inspire others and make the world shine with positivity!",
        "✨ Together, we create a brighter future. ✨"
    ]
    encouragements = [
        "Keep going, kindness champion!",
        "You're making the world better!",
        "Every guess is a step toward positivity!",
        "Kind hearts always win!"
    ]

    print("Welcome to the Kindness Game!")
    score = 0
    rounds = 3

    for level in range(1, rounds + 1):
        print(f"\nLevel {level}:")
        print("Guess a number between 1 and 100.")

        try:
            guess = int(input("Your guess: "))
            if 1 <= guess <= 100:
                chosen = random.randint(1, 100)
                print(f"\nThe kindness number is: {chosen}")
                if guess == chosen:
                    print("🎉 You guessed correctly! Spread the kindness! 🎉")
                    score += 1
                else:
                    print("Good try! Keep being kind!")
                print(random.choice(encouragements))
                print(messages[random.randint(0, len(messages) - 1)])
            else:
                print("Invalid number. Skipping this round.")
        except ValueError:
            print("Please enter a valid number. Skipping this round.")

    print(f"\nGame Over! Your kindness score: {score}/{rounds}")
    if score == rounds:
        print("Amazing! You're a true kindness hero!")
    elif score > 0:
        print("Great job! Keep spreading kindness!")
    else:
        print("Don't worry, kindness is always worth trying!")

if __name__ == "__main__":
    we_must_be_nice()