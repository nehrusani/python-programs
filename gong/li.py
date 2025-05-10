"""
this is for printing just strings but is not allowing numeric numbers.
"""
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        print("You typed:", name)
        continue
    print("Not possible! Please enter only alphabetic characters.")