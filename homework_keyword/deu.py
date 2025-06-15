num_of_an_amount = int(input("Enter the number of an amount: "))
percentage = int(input("Enter the percentage: "))
def calculate_percentage(num_of_an_amount, percentage):
    return (num_of_an_amount * percentage) / 100
result = calculate_percentage(num_of_an_amount, percentage)
print("The result is:", result)

#This code calculates the percentage of a given amount.
#It takes two inputs: the amount and the percentage to be calculated.
#The function `calculate_percentage` computes the percentage of the amount.