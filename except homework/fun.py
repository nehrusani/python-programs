from datetime import datetime

def age_counter(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

if __name__ == "__main__":
    try:
        birth_year = int(input("Enter your birth year: "))
        age = age_counter(birth_year)
        print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid year.")