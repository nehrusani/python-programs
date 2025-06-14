def shutdown (name):
    if n.lower() == "yes":
        print("Shutting down the laptop...")
    elif n.lower() == "no":
        print("Shutdown cancelled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
n = input("Do you want to shut down the laptop? (yes/no): ")
shutdown(n)