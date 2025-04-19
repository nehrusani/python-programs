actualcost = float(input("enter the actual price of the product:"))
saleamount = float(input("enter the sale amount:"))
if (saleamount>actualcost):
    amount = saleamount-actualcost
    print("you have made a profit",amount)
else:
    print("you are in loss")