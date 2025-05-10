while True:
    subject = input("Enter first subject: ")
    subject2 = input("Enter second subject:")

    if subject.lower() == "english" and subject2.lower() == "maths":
        print("You selected:", subject + '\n' + "You selected:" + subject2)
    

    continue_choice = input("Do you want to continue? (yes/no): ")
    if continue_choice.lower() != "yes":
        print("Goodbye!")
        break