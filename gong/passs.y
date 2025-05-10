import getpass

def setup_password():
    password = getpass.getpass("Set your password: ")
    confirm_password = getpass.getpass("Confirm your password: ")
    
    if password == confirm_password:
        print("Password setup successful!")
        # You can save the password securely (e.g., hashed) if needed
    else:
        print("Passwords do not match. Try again.")

setup_password()