# In this programm we are going to learn how can we add things in a tuple by converting it to a list.
tuple1 = ["Raju","nastya","eli","Rajya"]
toll = list(tuple1)
tuple1[1] = "rajan"
tuple1 = tuple(tuple1)
print(tuple1)
#tuple is a immutable list. 
# immutable means when you write a code to add 1 more data type in tuple it will show you an error.
# tuple is also a list but it is just faster then the list and immutable.