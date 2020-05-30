import random

# Taking input from user
stake_amount = int(input("Enter stake amount : "))
goal_amount = int(input("Enter goal amount : "))
bet_amount = int(input("Enter bet amount : "))
number_of_times = int(input("Enter number of times you want to play : "))

# Variables
win_count = 0
loss_count = 0

# loop for iterating no of times
for index in range(1, number_of_times+1):
    random_win = random.randint(0, 1)
    if random_win == 0:
        stake_amount -= bet_amount
        loss_count += 1
    else:
        stake_amount += bet_amount
        win_count += 1

# Calculating win and loss percentage
win_percentage = win_count*100/number_of_times
print("win percentage is:", win_percentage)
loss_percentage = loss_count*100/number_of_times
print("loss percentage is:", loss_percentage)



 