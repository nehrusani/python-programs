import getpass

correct_password="Sisi99009"
user_input=getpass.getpass("Enter your password:")

if user_input == correct_password:
    print("Acess granted")
else:
    print("incorrect password")