set1 = {1,3,4,6}
set2 = {3,4,5,2}

while True:
    gogo = set1.symmetric_difference(set2)
    print("Set1 :", set1)
    print("Set2 :", set2)
    print("the symmetric difference is :", gogo)
    dm = input("Do you want to repeat? (yes/no): ").strip().lower()
    if dm != "yes":
        break