#! /usr/bin/python

import TicTacToe 
import Button 



Game=TicTacToe.TicTacToe()


'''
def PlayAgain():
    print("Do You Want to Play Again???")
    Choice=str(raw_input("Enter Choice: "))
    
    if Choice=='Y' or Choice=="Yes" or Choice=='y' or Choice=="yes":
        return True 
    else:
        return False    



while True:
       
    while True:
        print("Player 1 Turn - 'O'")
        Game.PlayerInput("O")
        if Game.WinCheck("O"):
            print("####################")
            print("Player 1 Win!!!, GG")
            print("####################")           
            break
    
        if Game.DrawCheck():
            print("####################")
            print("DRAW!!!")
            print("####################")
            break 

        print("Player 2 Turn - 'X'")
        Game.PlayerInput("X")
        if Game.WinCheck("X"):
            print("####################")
            print("Player 2 Win!!!, GG")
            print("####################")
            break

        
        
    if PlayAgain():
        del Game
        Game=TicTacToe.TicTacToe()
        continue
    else:
        print("Thanks For Playing :D")
        break
'''