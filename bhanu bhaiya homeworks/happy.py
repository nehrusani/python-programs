# print length of the below list
"""lists = [1,2,'v',4,5,16]
print(len(lists))
# print 5th element of the below list
lists2 = [1,2,3,4,5,6]
print(lists2[4])
#print first and last character of the string
string = 'ditya:saini'
print(len(string)-1)
print(string[len(string)-1])
print(string[0])
#print from string
string = input('Enter a string: ')
if string:
    print(string[-1])
else:
    print('')
#print length and 3rd character of below string
string2 = 'abcdefg/)9'
print(len(string2))
print(string2[2])"""

# Print each character of a string on its own line
# Example output:
# D
# I
# T
"""
Read a list of integers from input (space-separated) and print their squares.
Example input: 1 2 3
Output: [1, 4, 9]
"""


"""s = str(input("enter your favourite word : "))
for ch in range(len(s)-1,-1,-1):
    print(s[ch])"""

"""s = str(input("enter your favourite word : "))
vowels = "aeiouAEIOU"
for ch in s:s:
        filtered += ch
reversed_string = filtered[::-1]
print(reversed_string)
    if ch not in vowels:
        print(ch)
for i in range(len(s)):
    ch = s[i]
    if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A' and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U':
        print(ch)    """


"""string = str(input("enter the word : "))
#lists = ['asdfasdf','second',3,4,'zuhz']
vowel ='aeiouAEIOU'
count = 0
for i in string : 
    if i not in vowel:
        count = count + 1
print(count)
print(oct(67))"""

take = input()
for i in range(len(take)):
    print(int(take[i])*int(take[i]))

# Reverse a string but remove the vowels
"""string = input("Enter a string: ")
var    = ""
for i in range(len(string)-1,-1,-1):
    var +=string[i]
print(var)
#print(var)
string = input()
vowels = "AEIUOaeiou"
vowels_count = 0
consonennt_count = 0
for i in range(len(string)):
    if string[i] not in vowels:
        consonennt_count += 1
    else :
        vowels_count     += 1
print("vowels:",vowels_count,"","consonennts:",consonennt_count)"""


