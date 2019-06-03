#! /usr/bin/python

class TicTacToe:

    Board=list()

    def __init__(self):
        self.Board=[" "]*10
        print("\n"*100)
        print("Welcome To Tic Tac Toe")
        print("\n\n")

        self.Board[0]='1'
        self.PrintBoard()

    def PrintBoard(self):
    
        print("     |     |   ")
        print("   "+self.Board[7]+" |  "+self.Board[8]+"  |  "+self.Board[9]+" ")
        print("7    |8    |9  ")
        print("----------------")
        print("     |     |   ")
        print("   "+self.Board[4]+" |  "+self.Board[5]+"  |  "+self.Board[6]+" ")
        print("4    |5    |6  ")
        print("----------------")
        print("     |     |   ")
        print("   "+self.Board[1]+" |  "+self.Board[2]+"  |  "+self.Board[3]+" ")
        print("1    |2    |3  ")
        print("\n")


    def WinCheck(self,Marker):
        self.PrintBoard()
        if self.Board[1]==Marker and self.Board[2]==Marker and self.Board[3]==Marker:
            return True 
        elif self.Board[4]==Marker and self.Board[5]==Marker and self.Board[6]==Marker:
            return True 
        elif self.Board[7]==Marker and self.Board[8]==Marker and self.Board[9]==Marker:
            return True 
        elif self.Board[1]==Marker and self.Board[5]==Marker and self.Board[9]==Marker:
                return True 
        elif self.Board[3]==Marker and self.Board[5]==Marker and self.Board[7]==Marker:
                return True 
        elif self.Board[1]==Marker and self.Board[4]==Marker and self.Board[7]==Marker:
            return True 
        elif self.Board[2]==Marker and self.Board[5]==Marker and self.Board[8]==Marker:
            return True 
        elif self.Board[3]==Marker and self.Board[6]==Marker and self.Board[9]==Marker:
            return True 
        else:
            return False


    def PlayerInput(self, Marker):
        while True:
            Position=int(input("Enter Position To Place Your Marker: "))

            if self.Board[Position]==" ":
                self.Board[Position]=Marker
                break
            else:
                print("Enter Valid Position ")
      
    def DrawCheck(self):
        for Index in self.Board:
            if Index==" ":
                return False 

        return True
    