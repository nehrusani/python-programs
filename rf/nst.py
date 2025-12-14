a = "Nehru"
b = "Nidhi"
c = "Ditya"
name_list = ["My name is Ditya", "My name is Saini", "My name is Saini", "My name is nidhi saini", "My name is nehru"]

# Count all items that start with "My name is"
count = sum(1 for name in name_list if name.startswith("My name is"))

print("The phrase 'My name is' appears", count, "times in the list.")
print(f"my name is {a} {b} {c} saini")