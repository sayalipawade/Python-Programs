import random
board=[0,1,2,3,4,5,6,7,8,9]

#Variables
symbol=0
player=" "
cell_count=0
maximum_cell=9
computer="O"
user="X"

class Tic_Tac_Toe:
    #Display board
    def print_board(self):
        print(board[1],'|',board[2],'|',board[3])
        print('----------')
        print(board[4],'|',board[5],'|',board[6])
        print('----------')
        print(board[7],'|',board[8],'|',board[9])

    #Assign symbol to players
    def assign_symbol(self):
        user="X"
        computer="O"

    #Toss for who play first    
    def switch_player(self):
        random_no=random.randint(0,1)
        if random_no == 1:
            self.user_play()
        else:
            print('computer will play')

    #Function for player
    def user_play(self):
        global cell_count
        if cell_count < maximum_cell:
            position=int(input("Enter Position:"))
            if board[position] == position:
                board[position]=user
                cell_count=cell_count+1
                self.print_board()
            else:
                print("Invalid Cell")
                self.user_play()
        else:
            print("Game Tie!!!")

tic_tac_toe=Tic_Tac_Toe()
tic_tac_toe.print_board()
tic_tac_toe.assign_symbol()
tic_tac_toe.switch_player()