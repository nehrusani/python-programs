from pubg import PUBGEligibility

age = int(input("Enter your age: "))

player = PUBGEligibility(age)
print(player.get_answer())