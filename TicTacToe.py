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
        self.Buttons=[" "]*9   
        self.win=pygame.display.set_mode((ResolutionX,ResolutionY))     
        self.InitialiseButtons()

    def RedrawWindow(self):
        self.win.fill((255,255,255))

    def InitialiseButtons(self):   
        #                  0                  1                   2                 3                   4                   5                 6                 7                  8                              
        Positions=[(0*Width,0*Height),(1*Width,0*Height),(2*Width,0*Height),(0*Width,1*Height),(1*Width,1*Height),(2*Width,1*Height),(0*Width,2*Height),(1*Width,2*Height),(2*Width,2*Height)]
        
        for Index in range(0,9):
            self.Buttons[Index]=Button.button((0,255,0),Positions[Index][0]+Offset,Positions[Index][1]+Offset,Width,Height," ")
    
            


    def DisplayButtons(self):
        Turn=0
        bWon=False 
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
                        
                    if self.Buttons[Index].bEmpty==False:
                        continue

                    if event.type==pygame.MOUSEBUTTONDOWN:
                       if self.Buttons[Index].isOver(pos):                                
                            if Turn==0:
                                self.Buttons[Index].AssignMarker("O")
                                bWon=self.WinCheck("O")
                                if bWon==True:
                                    return "O"                            
                            elif Turn==1:
                                self.Buttons[Index].AssignMarker("X")
                                bWon=self.WinCheck("X")
                                if bWon==True:
                                    return "X"
                            Turn=(Turn+1)%2 
                                      
                            if self.DrawCheck()==True:
                                return "Draw"
                            self.Buttons[Index].bEmpty=False
                    if self.Buttons[Index].bEmpty==False:
                        continue

                         
                    if event.type==pygame.MOUSEMOTION:
                        if self.Buttons[Index].isOver(pos):
                            self.Buttons[Index].color=(255,0,0)
                        else:
                            self.Buttons[Index].color=(0,255,0)
            
            
    def WinCheck(self,Marker):
        
        if self.Buttons[0].text==Marker and self.Buttons[1].text==Marker and self.Buttons[2].text==Marker:
            return True 
        elif self.Buttons[3].text==Marker and self.Buttons[4].text==Marker and self.Buttons[5].text==Marker:
            return True 
        elif self.Buttons[6].text==Marker and self.Buttons[7].text==Marker and self.Buttons[8].text==Marker:
            return True 
        elif self.Buttons[0].text==Marker and self.Buttons[4].text==Marker and self.Buttons[8].text==Marker:
                return True 
        elif self.Buttons[2].text==Marker and self.Buttons[4].text==Marker and self.Buttons[6].text==Marker:
                return True 
        elif self.Buttons[0].text==Marker and self.Buttons[3].text==Marker and self.Buttons[6].text==Marker:
            return True 
        elif self.Buttons[1].text==Marker and self.Buttons[4].text==Marker and self.Buttons[7].text==Marker:
            return True 
        elif self.Buttons[2].text==Marker and self.Buttons[5].text==Marker and self.Buttons[8].text==Marker:
            return True 
        else:
            return False


    def DrawCheck(self):
        for Index in range(0,9):
            if self.Buttons[Index].text==" ":
                return False 

        return True
    