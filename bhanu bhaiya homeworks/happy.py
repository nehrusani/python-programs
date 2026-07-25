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

data = input()
nums = [int(x) for x in data]
squares = [n*n for n in nums]
print(squares)
"""s = str(input("enter your favourite word : "))
for ch in s:
    print(ch)"""






