"""Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple"""
tuple_1 = ("teacher","student","class",1,5,6,1.5,1.7)
tuple_2 = (4,8,9,0)
tuple_3 = tuple_2 + (9,)
print(tuple_3)
tuple_4 = (1,4,6,1,1,6,4)
print(tuple_4.count(1))
print(tuple_1[1:4])