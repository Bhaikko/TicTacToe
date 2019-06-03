#! /usr/bin/python

import TicTacToe 

Game=TicTacToe.TicTacToe()
bGameOver=False

while True:
    
    while True:
        bOutcome=Game.DisplayButtons()
        if bOutcome == "O":
            print("Player 1 Won,GG")
            bGameOver=True
            break
        elif bOutcome == "X":
            print("Player 2 Won,GG")
            bGameOver=True
            break 
        elif bOutcome == "Draw":
            print("Draw,GG")
            bGameOver=True
            break
    if bGameOver==True:
        break    
    
   


'''
def PlayAgain():
    print("Do You Want to Play Again???")
    Choice=str(raw_input("Enter Choice: "))
    
    if Choice=='Y' or Choice=="Yes" or Choice=='y' or Choice=="yes":
        return True 
    else:
        return False    

        
        
    if PlayAgain():
        del Game
        Game=TicTacToe.TicTacToe()
        continue
    else:
        print("Thanks For Playing :D")
        break
'''