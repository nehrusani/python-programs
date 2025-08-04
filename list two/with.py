#this is the programm to find out minimum and maximum function but just without using max and min builtin function!!!
tup=("test122222222222222222222222222","test123","test12345", "test11221111199000000999999999999999")
for i in (tup):
    print(len(i))
max_len = len(tup)
max_word = tup
for big in tup:
    if len(big) > max_len :
        max_len = len(big)
        max_word = big
print("Word with most length:", max_word)
# Find the word with minimum length without using min() function
min_len = len(tup[0])
min_word = tup[0]
for word in tup:
    if len(word) < min_len:
        min_len = len(word)
        min_word = word
print("Word with less length:", min_word)