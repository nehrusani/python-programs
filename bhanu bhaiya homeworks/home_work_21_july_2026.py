"""p = 0
for i in range(21):
    p = p+i # p = 10 + 1
print(p)"""

# code two as you said it swaps variable
"""a = 10
b = 2
print('before swap:', a, b)
temp = a
a = b
b = temp
print('after swap:', a, b)"""

#code three as you said it checks vowels
"""tell = input("enter a word : ")
vowels = "aeiouAEIOU"
found = [ch for ch in tell if ch in vowels]
if found:
    print("Vowels found:", " ".join(found))
else:
    print("No vowels found")"""

#code four as you said this pattern
"""for i in range(3, 0,-1):
    print("* " * (i * 3))
print("reverse pattern")"""

string = str(input("enter any type of word or no existing word : "))
rev    = ""
for i in range(len(string)-1,-1,-1):
    #string2 = string + string[i]
    rev = rev+string[i]
    #print(string[len(i)-1])
print(rev)
print()

