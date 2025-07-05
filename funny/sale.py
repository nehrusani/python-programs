import random

def sale_game():
    print("Welcome to the Crazy Sale Game!")
    items = ["Laptop", "Phone", "Headphones", "Camera", "Watch"]
    prices = {item: random.randint(50, 500) for item in items}
    wallet = 1000
    cart = []

    print(f"\nYou have ${wallet} to spend.\n")
    print("Items for sale:")
    for item in items:
        print(f"- {item}: ${prices[item]}")

    while wallet > 0 and items:
        choice = input("\nEnter the name of the item to buy (or 'quit' to exit): ").strip()
        if choice.lower() == 'quit':
            break
        if choice in items:
            if prices[choice] <= wallet:
                wallet -= prices[choice]
                cart.append(choice)
                items.remove(choice)
                print(f"You bought {choice}! Remaining money: ${wallet}")
            else:
                print("Not enough money for that item.")
        else:
            print("Item not available.")

    print("\nGame Over!")
    print(f"Items bought: {cart}")
    print(f"Money left: ${wallet}")

if __name__ == "__main__":
    sale_game()