import datetime

# Resident Permit Program

def apply_for_permit():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    
    if age >= 18:
        permit_id = f"RP{datetime.datetime.now().strftime('%Y%m%d')}"
        print(f"\nPermit approved for {name}")
        print(f"Permit ID: {permit_id}")
        print(f"Address: {address}")
        print(f"Valid for 5 years")
    else:
        print("Error: Must be 18 or older to apply")

if __name__ == "__main__":
    apply_for_permit()