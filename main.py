#! /usr/bin/python

import TicTacToe 
import time


TicTacToeGame=TicTacToe.TicTacToe()
bGameOver=False

while True:
    
    while True:        
        bOutcome=TicTacToeGame.Menu()
        if bOutcome == "O":
            TicTacToeGame.WinScreen(1)
            bGameOver=True
            break
        elif bOutcome == "X":
            TicTacToeGame.WinScreen(2)
            bGameOver=True
            break 
        elif bOutcome == "Draw":
            TicTacToeGame.WinScreen(3)
            bGameOver=True
            break
        
    if bGameOver==True:   
        del TicTacToeGame
        TicTacToeGame=TicTacToe.TicTacToe()    
        time.sleep(2)
           
    
   

