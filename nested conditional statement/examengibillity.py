x = input("Did the student have a medical cause  ('Y' for yes and 'N' for no). ")
v = int(input("Enter the attendance of the stundent :"))
if x == "Y":
    print("student can attend the exam")
else:
    if v >= 75:
        print("allowed")
    else:
        print("student is not allowed")
        # We used nested if in else but you can also use it in if it self
  