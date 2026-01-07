# Odd–Even Checker

numbers = input("Enter numbers separated by spaces: ").split()

odd_count = 0
even_count = 0

for n in numbers:
    num = int(n)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
