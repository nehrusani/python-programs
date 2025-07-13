my_dict = {'Nastya':2,'Manoj':6,'Nastya':2,'jack':2}
k = 2
r = 0
for key in my_dict:
    if my_dict[key]== k:
        r = r + 1
print(f"the freequeency of {k} is {r}")