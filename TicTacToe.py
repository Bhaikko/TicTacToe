def PrintBoard(Board):
    Board[0]='1'
    print("     |     |   ")
    print("   "+Board[7]+" |  "+Board[8]+"  |  "+Board[9]+" ")
    print("7    |8    |9  ")
    print("----------------")
    print("     |     |   ")
    print("   "+Board[4]+" |  "+Board[5]+"  |  "+Board[6]+" ")
    print("4    |5    |6  ")
    print("----------------")
    print("     |     |   ")
    print("   "+Board[1]+" |  "+Board[2]+"  |  "+Board[3]+" ")
    print("1    |2    |3  ")
    print("\n")

def SpaceCheck(Board,Position):
    return Board[Position]==" "

def PlayerInput(Marker):
   
    while True:
        Position=int(input("Enter Position To Place Your Marker: "))

        if SpaceCheck(Board,Position):
            Board[Position]=Marker
            break
        else:
            print("Enter Valid Position ")
      

def WinCheck(Board,Marker):
    PrintBoard(Board)
    if Board[1]==Marker and Board[2]==Marker and Marker[3]==Marker:
        return True 
    elif Board[4]==Marker and Board[5]==Marker and Board[6]==Marker:
        return True 
    elif Board[7]==Marker and Board[8]==Marker and Board[9]==Marker:
        return True 
    elif Board[1]==Marker and Board[5]==Marker and Board[9]==Marker:
            return True 
    elif Board[3]==Marker and Board[5]==Marker and Board[7]==Marker:
            return True 
    elif Board[1]==Marker and Board[4]==Marker and Board[7]==Marker:
        return True 
    elif Board[2]==Marker and Board[5]==Marker and Board[8]==Marker:
        return True 
    elif Board[3]==Marker and Board[6]==Marker and Board[9]==Marker:
        return True 
    else:
        return False

def DrawCheck(Board):
    for Index in Board:
        if Index==" ":
            return False 

    return True

def PlayAgain():
    print("Do You Want to Play Again???")
    Choice=str(input("Enter Choice: ")).lower()
    
    if Choice=="yes" or Choice=="y":
        return True 
    else:
        return False    

Board=[" "]*10

while True:
    print("\n"*100)
    print("Welcome To Tic Tac Toe")
    print("\n\n")
    PrintBoard(Board)

    while True:
        
        print("Player 1 Turn - 'O'")
        PlayerInput("O")
        if WinCheck(Board,"O"):
            print("####################")
            print("Player 1 Win!!!, GG")
            print("####################")           
            break
  
        if DrawCheck(Board):
            print("####################")
            print("DRAW!!!")
            print("####################")
            break 

        print("Player 2 Turn - 'X'")
        PlayerInput("X")
        if WinCheck(Board,"X"):
            print("####################")
            print("Player 2 Win!!!, GG")
            print("####################")
            break

       
       
    if PlayAgain():
        Board=[" "]*10
        continue
    else:
        break


