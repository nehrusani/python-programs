my_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(my_dict)
k = 2

r = 0
for key in my_dict:
    if my_dict[key]== k :
        r = r + 1
print("frequenssy of k is " +str(r))