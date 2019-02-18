def PrintBoard(Board):
    print("     |     |   ")
    print("   "+Board[7]+" |  "+Board[8]+"  |  "+Board[9]+" ")
    print("     |     |   ")
    print("----------------")
    print("     |     |   ")
    print("   "+Board[4]+" |  "+Board[5]+"  |  "+Board[6]+" ")
    print("     |     |   ")
    print("----------------")
    print("     |     |   ")
    print("   "+Board[1]+" |  "+Board[2]+"  |  "+Board[3]+" ")
    print("     |     |   ")
    print("\n\n\n")

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
            Position=int(input("Enter Position To Place Your Marker: "))

def WinCheck(Board,Marker):
    if Board[1]==Marker and Board[2]==Marker and Marker[3]:
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

Board=[" "]*10

while True:
    
    print("Welcome To Tic Tac Toe")

    while True:
        PrintBoard(Board)
        print("Player 1 Turn")
        PlayerInput("O")
        WinCheck(Board,"O")

        PrintBoard(Board)
        print("Player 2 Turn")
        PlayerInput("X")
        WinCheck(Board,"X")

        


