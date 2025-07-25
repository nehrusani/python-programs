import psutil
for i in range (1,10):
    if i == 5:
        test = psutil.virtual_memory
        print("exit")
        exit()
    print(i)