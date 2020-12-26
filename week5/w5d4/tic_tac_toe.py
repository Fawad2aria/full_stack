class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token

class Board():

    def __init__(self):
        self.spaces = [' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def __repr__(self): 

        line1 = self.spaces[1] + " | " + self.spaces[2] + " | " + self.spaces[3]
        line2 = self.spaces[4] + " | " + self.spaces[5] + " | " + self.spaces[6]
        line3 = self.spaces[7] + " | " + self.spaces[8] + " | " + self.spaces[9]
        return line1 + '\n' + line2 + '\n' + line3


    def place_token(self, token, position):

        if self.spaces[position] != " ":
            print("Invalid move. Space is taken, and you lost your move.")
        else:
            self.spaces[position] = token
    
    def cal_winner(self, player):

        if self.spaces[1] == player and self.spaces[2]==player and self.spaces[3]==player:
            return True
        
        if self.spaces[4] == player and self.spaces[5]==player and self.spaces[6]==player:
            return True

        if self.spaces[7] == player and self.spaces[8]==player and self.spaces[9]==player:
            return True
        
        if self.spaces[1] == player and self.spaces[4]==player and self.spaces[7]==player:
            return True

        if self.spaces[2] == player and self.spaces[5]==player and self.spaces[8]==player:
            return True

        if self.spaces[3] == player and self.spaces[6]==player and self.spaces[9]==player:
            return True
        
        if self.spaces[1] == player and self.spaces[5]==player and self.spaces[9]==player:
            return True

        if self.spaces[3] == player and self.spaces[5]==player and self.spaces[7]==player:
            return True
        return False
        
    
    def is_full(self):
        used_spaces = 0
        for space in self.spaces:
            if space != " ":
                used_spaces += 1
        
        if used_spaces == 9:
            return True
        else:
            return False

    def is_game_over(self):
        return self.cal_winner('X') or self.cal_winner('O') or self.is_full()


def main():
    board = Board()
    player1 = Player(input('Enter you name Player1: '), 'X')
    player2 = Player(input('Enter your name Player2 '), 'O')
    player = player1


    while not board.is_game_over():

        position = int(input(f'{player.name}: Please choose from 1 - 9: '))
        board.place_token(player.token, position)
        print(board)

        if player == player1:
            player = player2
        elif player == player2:
            player = player1
        

    if board.cal_winner("X"):
        print(f"\n{player1} wins!")
    
    elif board.cal_winner("O"):
        print(f"\n{player2} wins!\n")
    
    else:
        print("\nYou are both tie!\n")


main()

