#! /usr/bin/python
import Button 
import pygame
import time 


ResolutionX=800
ResolutionY=600

Height=100
Width=100
Offset=200

class TicTacToe:
    def __init__(self):
        self.Buttons=[" "]*9  
        self.bDark=False 
        self.Background=(255,255,255)
        self.ButtonClicked=(255,0,0)
        self.ButtonDefault=(0,255,0)
        self.InitialiseWindows()        
        self.InitialiseButtons()

    def InitialiseWindows(self):
        self.win=pygame.display.set_mode((ResolutionX,ResolutionY))  
        self.menu=pygame.display.set_mode((ResolutionX, ResolutionY))   
        self.End=pygame.display.set_mode((ResolutionX, ResolutionY))

    def InitialiseButtons(self):   
        self.Start=Button.button((0,255,0),150,200,400,100,"Start")
        self.Exit=Button.button((0,255,0),250,350,200,75,"Exit")
        self.Reset=Button.button((0,255,0),550,525,175,50,"Reset")
        self.DarkMode=Button.button((0,255,0),500,525,250,50,"Dark Mode")

        #                  0                  1                   2                 3                   4                   5                 6                 7                  8                              
        Positions=[(0*Width,0*Height),(1*Width,0*Height),(2*Width,0*Height),(0*Width,1*Height),(1*Width,1*Height),(2*Width,1*Height),(0*Width,2*Height),(1*Width,2*Height),(2*Width,2*Height)]
        
        for Index in range(0,9):
            self.Buttons[Index]=Button.button((0,255,0),Positions[Index][0]+Offset,Positions[Index][1]+Offset,Width,Height," ")
    

    def Menu(self):
        self.menu.fill(self.Background)

        while True:
            
            self.Start.draw(self.menu,(0,0,0))
            self.Exit.draw(self.menu,(0,0,0))
            self.DarkMode.draw(self.menu,(0,0,0))
                
            pygame.display.update()
            self.ShowText("Welcome To TicTacToe",True,(100,100),self.menu)
            
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                        
                if event.type==pygame.MOUSEBUTTONDOWN: 
                   if self.Start.isOver(pos):
                       del self.win
                       self.win=pygame.display.set_mode((ResolutionX,ResolutionY))
                       return self.Game()  
                   if self.DarkMode.isOver(pos):
                        if self.bDark==False:
                            self.DarkMode.AssignMarker("Light Mode")
                            self.Background=(80,80,80)
                            self.ButtonClicked=(125,30,30)
                            self.ButtonDefault=(30,125,30)
                            self.bDark=True

                        elif self.bDark==True:
                            self.DarkMode.AssignMarker("Dark Mode")
                            self.Background=(255,255,255)
                            self.ButtonClicked=(255,0,0)
                            self.ButtonDefault=(0,255,0)
                            self.bDark=False

                   if self.Exit.isOver(pos):      
                       pygame.quit()
                       quit()

                                    
                if event.type==pygame.MOUSEMOTION:
                    if self.Start.isOver(pos):
                        self.Start.color=(self.ButtonClicked)
                    else:
                        self.Start.color=(self.ButtonDefault)

                    if self.Exit.isOver(pos):
                        self.Exit.color=(self.ButtonClicked)
                    else:
                        self.Exit.color=(self.ButtonDefault)

                    if self.DarkMode.isOver(pos):
                        self.DarkMode.color=(self.ButtonClicked)
                    else:
                        self.DarkMode.color=(self.ButtonDefault)
            
    def Game(self):
        Turn=0
        bWon=False 
        self.win.fill(self.Background)

        while True:
            
            for Index in range(0,9):
                self.Buttons[Index].draw(self.win,(0,0,0))
            self.Reset.draw(self.win,(0,0,0))    

            pygame.display.update()
            
            self.ShowText(Turn+1,False,(ResolutionX/4,ResolutionY/5),self.win)
            
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                       

                for Index in range(0,9):
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                        
                    if self.Buttons[Index].bEmpty==False:
                        continue

                    if event.type==pygame.MOUSEBUTTONDOWN:

                       if self.Reset.isOver(pos):
                            return "Reset"

                       if self.Buttons[Index].isOver(pos):                                
                            if Turn==0:
                                self.Buttons[Index].AssignMarker("O")
                                bWon=self.WinCheck("O")
                                if bWon==True:   
                                    for Index in range(0,9):
                                        self.Buttons[Index].draw(self.win,(0,0,0))
                                    pygame.display.update()
                                    time.sleep(2)                                                           
                                    return "O"                            
                            elif Turn==1:
                                self.Buttons[Index].AssignMarker("X")
                                bWon=self.WinCheck("X")
                                if bWon==True:  
                                    for Index in range(0,9):
                                        self.Buttons[Index].draw(self.win,(0,0,0))
                                    pygame.display.update()    
                                    time.sleep(2)                                      
                                    return "X"
                            Turn=(Turn+1)%2 
                                      
                            if self.DrawCheck()==True: 
                                for Index in range(0,9):
                                        self.Buttons[Index].draw(self.win,(0,0,0))
                                pygame.display.update()    
                                time.sleep(2)                                                               
                                return "Draw"

                            self.Buttons[Index].bEmpty=False

                    if self.Buttons[Index].bEmpty==False:
                        continue
                    

                         
                    if event.type==pygame.MOUSEMOTION:
                        if self.Buttons[Index].isOver(pos):
                            self.Buttons[Index].color=(self.ButtonClicked)
                        else:
                            self.Buttons[Index].color=(self.ButtonDefault)

                        if self.Reset.isOver(pos):
                            self.Reset.color=(self.ButtonClicked)
                        else:
                            self.Reset.color=(self.ButtonDefault)

    def WinScreen(self,Text):
        self.End.fill(self.Background)

        while True:       
                     
            
            if Text==1:
                self.ShowText("Player 1 Won, GG",True,(ResolutionX/4,ResolutionY/2),self.End)
            elif Text==2:
                self.ShowText("Player 2 Won, GG",True,(ResolutionX/4,ResolutionY/2),self.End)
            else:
                self.ShowText("Draw, GG",True,(ResolutionX/4,ResolutionY/2),self.End)
            pygame.display.update()
            time.sleep(3)
            break
                        
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

    def ShowText(self,Text,Menu,Coordinates,Screen):
        font = pygame.font.SysFont('comicsans', 70)
        if Menu==False:
            text = font.render("Player " + str(Text) + " Turn", True, (0,0,0))  
        else:
            text = font.render(str(Text), True, (0,0,0))

        Screen.fill(self.Background)      
        Screen.blit(text, Coordinates)
        