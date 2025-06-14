def total_calc(billamount,tip_perc):
    total = billamount * (1+0.01*tip_perc)
    total = round(total,2)
    print(f"pleas pay{total}")
total_calc(9000,10)