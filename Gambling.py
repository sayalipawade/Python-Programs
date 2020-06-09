import random

# Variables
win_count = 0
loss_count = 0
stake_amount = 0
goal_amount = 0
bet_amount = 0

#Constants
NUMBER_OF_TIMES=20

class GamblingSimulator:

    # Taking input from user
    def take_input(self):
        try:
            stake_amount = int(input("Enter stake amount : "))
            goal_amount = int(input("Enter goal amount : "))
            bet_amount = int(input("Enter bet amount : "))
        except ValueError:
            print('Invalid value')
        except:
            print('Something else went wrong')
        
    # user playing game
    def play_game(self):
        global NUMBER_OF_TIMES
        global stake_amount
        global goal_amount
        global win_count
        global loss_count
        for index in range(1, NUMBER_OF_TIMES+1):
            random_win = random.randint(0, 1)
            if random_win == 0:
                stake_amount -= bet_amount
                loss_count += 1
            else:
                stake_amount += bet_amount
                win_count += 1

    #Percentage for win and loss
    def calculate_percentage(self):
        try:
            win_percentage = win_count*100/NUMBER_OF_TIMES
            print("win percentage is:", win_percentage)
            loss_percentage = loss_count*100/NUMBER_OF_TIMES
            print("loss percentage is:", loss_percentage)
        except ZeroDivisionError:
            print('Divide by zero exception')

#Creating object of class
gambler=GamblingSimulator()

#Function Calling
gambler.take_input()
gambler.play_game()
gambler.calculate_percentage()





 