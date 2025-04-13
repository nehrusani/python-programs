amount=int(input("enter the amout to be widrewn from the atm"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//20
print("notes of 100 rupees",note1)
print("notes of 50 rupees",note2)
print("notes of 20 rupees",note3)