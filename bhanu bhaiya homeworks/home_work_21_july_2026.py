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


"""word = str(input("enter your word : "))  #laptop
word1 = ""
for i in range(len(word)-1,-1,-1): #
    word1 = word1+word[i]
print("after reverse",word1)"""



"""
sum = 0
i = 1
while i <= 15:
    sum += i # p=p+i
    i += 1  # i=i+1
print(sum) 
"""

"""marks = int(input("enter your marks of the test : "))
if marks >= 90 :
    print("you stand first ")
elif marks >= 80 and marks < 90 :
    print("you stand second")
elif marks >= 70 and marks < 80 :
    print("you stand third ")
else:
    print("you can improve")"""

"""num = 10
# print 2 times table from 1 to 10
while num >= 1:
    print(f"2 x {num} = {2 * num}")
    num -= 1"""


"""tell = input("enter a word : ")
vowels = "aeiouAEIOU"
num = 0
for i in range(len(tell)):
    if tell[i] in vowels:
        num += 1
if num == 0:
    print("sorry no vowels")
print(f"Number of vowels: {num}")"""

# pattern: 1\n#2 2\n 3 3 3\n 4 4 4 4\n 5 5 5 5 5
"""for i in range(1, 6,-1):
    print(' '.join([str(i)] * i))
    i -= 1"""

        
