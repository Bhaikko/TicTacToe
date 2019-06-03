#! /usr/bin/python
import Button 
import pygame 

ResolutionX=800
ResolutionY=600

Height=100
Width=100
Offset=200


class TicTacToe:

    Board=list()
    Buttons=list()

    def __init__(self):
        self.Board=[" "]*10
        self.Buttons=[" "]*10
        
        self.win=pygame.display.set_mode((ResolutionX,ResolutionY))     
        self.InitialiseButtons()
        self.Board[0]='1'

    def RedrawWindow(self):
        self.win.fill((255,255,255))

    def InitialiseButtons(self):   
        #                  1                  2                   3                 4                   5                   6                 7                 8                  9                              
        Positions=[(0*Width,0*Height),(0*Width,1*Height),(0*Width,2*Height),(1*Width,0*Height),(1*Width,1*Height),(1*Width,2*Height),(2*Width,0*Height),(2*Width,1*Height),(2*Width,2*Height)]
        for Index in range(0,9):
            self.Buttons[Index]=Button.button((0,255,0),Positions[Index][0]+Offset,Positions[Index][1]+Offset,Width,Height,"Click ME")
    
            


    def DisplayButtons(self):
        #for Index in range(0,9):
            while True:
                self.RedrawWindow()
                for Index in range(0,9):
                    self.Buttons[Index].draw(self.win,(0,0,0))
                
                pygame.display.update()
                
                for event in pygame.event.get():
                    pos=pygame.mouse.get_pos()

                    for Index in range(0,9):
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()
                        
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if self.Buttons[Index].isOver(pos):
                                print("Clicked")

                        if event.type==pygame.MOUSEMOTION:
                            if self.Buttons[Index].isOver(pos):
                                self.Buttons[Index].color=(255,0,0)
                            else:
                                self.Buttons[Index].color=(0,255,0)
                


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
    