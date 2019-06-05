#! /usr/bin/python

import TicTacToe 
import time


TicTacToeGame=TicTacToe.TicTacToe()
bGameOver=False

while True:
    
    while True:        
        bOutcome=TicTacToeGame.Menu()
        if bOutcome == "O":
            print("Player 1 Won,GG")
            TicTacToeGame.ShowText("Player 1 Won, GG",True,(400,300))
            bGameOver=True
            break
        elif bOutcome == "X":
            print("Player 2 Won,GG")
            TicTacToeGame.ShowText("Player 2 Won, GG",True,(400,300))
            bGameOver=True
            break 
        elif bOutcome == "Draw":
            print("Draw,GG")
            TicTacToeGame.ShowText("Draw, GG",True,(400,300))
            bGameOver=True
            break
        
    if bGameOver==True:   
        del TicTacToeGame
        TicTacToeGame=TicTacToe.TicTacToe()    
        time.sleep(2)
           
    
   

