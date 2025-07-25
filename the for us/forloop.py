attempts = 0
max_attempts = 2
while attempts < max_attempts:
    try:
        p = int(input("enter the 1 num : "))
        k = int(input("enter the 2 num : "))
        for i in range(p, k):
            print(i)
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        attempts += 1
else:
    print("Too many invalid attempts. Exiting.")
