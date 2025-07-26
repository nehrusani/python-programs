max_attempts = 2

def get_int_input(prompt):
    attempts = 0
    while attempts < max_attempts:
        try:
            return int(input(prompt))
        except Exception as e:
            print(f"An error occurred: {e}")
            attempts += 1
    print("Too many invalid attempts. Exiting.")
    exit()

p = get_int_input("enter the 1 num : ")
k = get_int_input("enter the 2 num : ")
for i in range(p, k):
    print(i)
