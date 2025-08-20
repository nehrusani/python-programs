word = str(input("enter a word : "))
vowels = "aeiouAEIOU"
count = sum(1 for char in word if char in vowels)
print("Number of vowels:", count)