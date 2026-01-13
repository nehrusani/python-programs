import time

def slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

slow("=== Welcome to the Problem Assistant ===")

while True:
    print("\nChoose your problem:")
    print("1. Blackmailing")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        slow("\n🕵️ Starting blackmail investigation...")
        time.sleep(0.5)

        print("\nWere you at home?")
        print("1. Yes")
        print("2. No")
        home = input("Enter choice: ")

        if home == "2":
            slow("\nWhere did you receive the call?")
            print("1. Market")
            print("2. Other place")
            loc = input("Enter choice: ")

            if loc == "1":
                slow("🛒 What was the market name?")
            else:
                slow("Please specify the location.")

        elif home == "1":
            slow("\nCan we check your phone?")
            print("1. Yes")
            print("2. No")
            phone = input("Enter choice: ")

            if phone == "2":
                slow("❗ We cannot help without your phone.")
            else:
                slow("🔍 Checking your phone...")
                time.sleep(1)
                slow("✔️ Scan complete.")

        else:
            slow("⚠️ Invalid choice.")

    elif choice == "2":
        slow("Goodbye!")
        break

    else:
        slow("Invalid option. Try again.")
