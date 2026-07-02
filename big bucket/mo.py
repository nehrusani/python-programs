boom_count = 0
for i in range(3):
    month = int(input("enter your own number 1-7 : "))
    match month:
        case 1:
            print("boom")
            boom_count += 1
        case 2:
            print("safe")
        case 3:
            print("safe")
        case 4:
            print("safe")
        case 5:
            print("safe")
        case 6:
            print("boom")
            boom_count += 1
        case 7:
            print("safe")
    if boom_count == 2:
        break

    
    
