import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def password_challenge():
    password = generate_password(10)
    print("Memorize this password:")
    print(password)
    input("Press Enter when you're ready to type it back...")
    guess = input("Enter the password: ")
    if guess == password:
        print("Correct! Well done.")
    else:
        print("Incorrect. The password was:", password)

if __name__ == "__main__":
    password_challenge()