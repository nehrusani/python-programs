from product import Product

p1 = Product("Laptop", 1200, ("Electronics", "Computers"))
p2 = Product("Shoes", 80, ("Fashion", "Footwear"))

products = [p1, p2]

# Print product info
for p in products:
    p.display_info()

# Category checks
if p1.is_in_category("Electronics"):
    print("Laptop is in Electronics category")
else:
    print("Laptop is NOT in Electronics category")

if p2.is_in_category("Electronics"):
    print("Shoes is in Electronics category")
else:
    print("Shoes is NOT in Electronics category")

print("\nAfter discount:")

# Apply 10% discount
p1.apply_discount(10)
p2.apply_discount(10)

print(f"Laptop new price: {p1.price}")
print(f"Shoes new price: {p2.price}")
