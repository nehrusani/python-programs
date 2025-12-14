# instead of writing a lot of time if...else you can also write match!!!
day = 4
match day:
  case 4:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")