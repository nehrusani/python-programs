num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:\n")

for i in range(1, 11):  # You can go up to any number you like
    print(f"{num} x {i} = {num * i}")