word = str(input("enter a word : "))
print(f"{sum(1 for c in word if c.isalpha())} alphabets are there")