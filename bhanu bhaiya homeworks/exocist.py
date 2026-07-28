number = 25
print("Guess a number from 1 to 50.")

for i in range(5):
    guess_str = input(f"Try {i+1}: ")
    if not guess_str.isdigit():
        print("Enter a valid integer.")
        continue
    guess = int(guess_str)
    if guess == number:
        print("You win!")
        break
else:
    print("Out of tries. The number was", number)