def hotel(nights):
    return 1000*nights
def flight(city):
    if city == "paris":
        return 10000
    elif city == "lyon":
        return 2000
    elif city == "Marseille":
        return 3000
def car(day):
    if day>7:
        return 6000*day
    elif day>3:
        return 6000*day
    else:
        return 6000*day
def totaltripcost(city,nights,day,spendingmoney):
    return flight(city)+hotel(nights)+car(day)+spendingmoney
print(totaltripcost("paris",7,5,3880))