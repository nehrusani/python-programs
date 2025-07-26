def get_valid_number(prompt):
    for attempt in range(2):  # Allow 2 attempts
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("Too many invalid attempts. Exiting.")
    exit()  # Exit after 2 invalid attempts

while True:
    x = get_valid_number("Enter the first number: ")
    y = get_valid_number("Enter the second number: ")

    for i in range(x, y):
        print(i)

    retry = input("Do you want to retry? (yes): ")
    if retry.lower() != "yes":
        print("Exiting the program...")
        break