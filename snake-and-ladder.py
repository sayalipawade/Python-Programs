import random
print("Welcome to snake and ladder")

#constants
STARTING_POSITION=0
WINNING_POSITION=100

#Variables
dice_roll=0
die_value = 0
player1=0
player2=0
win_time=0
player_position=STARTING_POSITION

class Snake_ladder:

    #Function for player moves
    def set_player_moves(self):
        win_time=0
        for index in range(0,WINNING_POSITION+1):
            die_value=random.randint(1,6)
            playing_option=random.randint(0,2)
            if playing_option == 0:
                self.no_play()
            elif playing_option == 1:
                win_time=win_time+1
                self.ladder()
            elif playing_option == 2:
                self.snake()
        return win_time

    #If user wants to no play
    def no_play(self):
        global player_position
        player_position=player_position

    #Function for ladder
    def ladder(self):
        player_position=0
        win_time=0
        player_position=player_position+die_value
       
        if player_position > WINNING_POSITION:
            player_position=player_position-die_value

    #Function for snake  
    def snake(self):
        player_position=0
        player_position=player_position-die_value
        if player_position < STARTING_POSITION:
            player_position=STARTING_POSITION

snake_ladder=Snake_ladder()
player1=snake_ladder.set_player_moves()
player2=snake_ladder.set_player_moves()

#Which player will win the game
if player1 < player2:
    print('player1 wins')
else:
    print('player2 wins')