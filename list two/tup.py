# we found out of max and min the tup using max and min built in function
tup=("dide","for","yeshj")
for i in (tup):
    print(len(i))
max_word = max(tup, key=len)
print("Word with most length:", max_word)
min_word = min(tup,key=len)
print("Word with less lenght:",min_word)