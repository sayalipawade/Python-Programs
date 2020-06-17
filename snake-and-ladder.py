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

#Dictionary
game_record={}

class Snake_ladder:
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

    def no_play(self):
        global player_position
        player_position=player_position

    def ladder(self):
        player_position=0
        win_time=0
        player_position=player_position+die_value
       
        if player_position > WINNING_POSITION:
            player_position=player_position-die_value
        
    def snake(self):
        player_position=0
        player_position=player_position-die_value
        if player_position < STARTING_POSITION:
            player_position=STARTING_POSITION

snake_ladder=Snake_ladder()
player1=snake_ladder.set_player_moves()
player2=snake_ladder.set_player_moves()

if player1 < player2:
    print('player1 wins')
else:
    print('player2 wins')