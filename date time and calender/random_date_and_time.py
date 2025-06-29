import random
import time
def rex(start_date,end_date):
    print(start_date,end_date)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"
    start_time=time.mktime(time.strptime(start_date,dateformat))
    end_time =time.mktime(time.strptime(end_date,dateformat))
    randomtime=start_time+randomgenerator*(end_time-start_time)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("randomdate:",rex("01/01/2025","01/01/3000"))