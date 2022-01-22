from typing import SupportsComplex
import pygame, sys
from pygame.locals import *


 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((600,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Marble Solitaire")
 
list = []

class Spot(pygame.sprite.Sprite):
    id = (0,0)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Richguy.png")
        self.rect = self.image.get_rect()
        self.isMarble = False
        self.isValidSpot = True
    def setPosition(self, num1, num2):
        self.rect.center = (num1,num2) 
        self.id = (num1, num2)
    def getX(self):
        return self.id[0]
    def getY(self):
        return self.id[1]
    def updates(self):
        co1 = self.id[0]
        co2 = self.id[1]
        self.draw(DISPLAYSURF,co1, co2)
    def draw(self, surface,num3,num4):
        self.setPosition(num3, num4)
        surface.blit(self.image, self.rect)
    def validSpot(self, list, num, num2):
        for item in list: 
            if item.isMarble and item.id[0] == num and item.id[1] == num2:
                self.isValidSpot = False
                return
            elif item.isMarble and item.id[0] != num and item.id[1] != num2:
                self.isValidSpot = True
    def validMove(self, x, y):
        return
    def whichDelete(self, x, y):
        pass
                

                


class Marble(pygame.sprite.Sprite):
    id = (0,0)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Poorman.png")
        self.rect = self.image.get_rect()
        self.clicked = False
        self.isMarble = True
        self.isValidSpot = False
    def setPosition(self, num1, num2):
        self.rect.center = (num1,num2) 
        self.id = (num1, num2)
    def updates(self):
        co1 = self.id[0]
        co2 = self.id[1]
        self.draw(DISPLAYSURF,co1, co2)
        if self.clicked == True:
            self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Poorman2.png")
        else:
            self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Poorman.png")
    def draw(self, surface,num3,num4):
        self.setPosition(num3, num4)
        surface.blit(self.image, self.rect) 
    def validSpot(self,list, num, num2):
        return
    def validMove(self, spotX, spotY):
        if self.id[0] == (spotX + 120) and spotY == self.id[1]:
            return True
        elif self.id[1] == (spotY + 120) and spotX == self.id[0]:
            return True
        elif self.id[0] == (spotX - 120) and spotY == self.id[1]:
            return True
        elif self.id[1] == (spotY - 120) and spotX == self.id[0]:
            return True
        else:
            return False
    def whichDelete(self, spotX, spotY):
        if self.id[0] == (spotX + 120) and spotY == self.id[1]:
            return spotX + 60, spotY 
        elif self.id[1] == (spotY + 120) and spotX == self.id[0]:
            return spotX, spotY + 60
        elif self.id[0] == (spotX - 120) and spotY == self.id[1]:
            return spotX - 60, spotY
        elif self.id[1] == (spotY - 120) and spotX == self.id[0]:
            return spotX, spotY - 60
        




# Creating Marbles and Spots
def createMarblesNew(spotOrMarble, startPointX, startPointY, number):
    endPointX = startPointX
    j = 0
    for j in range(1, number):
        endPointX += 60
        if spotOrMarble == 1:
            spot = Spot()
            list.append(spot)
            spot.setPosition(endPointX, startPointY)
        if spotOrMarble == 2:
            marble = Marble()
            list.append(marble)
            marble.setPosition(endPointX,startPointY)



#Creates the objects of the Spaces.
createMarblesNew(1,180,120,4)
createMarblesNew(1,120,180,6)
createMarblesNew(1,60,240,8)
createMarblesNew(1,180,480,4)
createMarblesNew(1,120,420,6)
createMarblesNew(1,60,360,8)
createMarblesNew(1,60,300,8)
#Creates the objects of the Marbles.
createMarblesNew(2,180,120,4)
createMarblesNew(2,120,180,6)
createMarblesNew(2,60,240,8)
createMarblesNew(2,180,480,4)
createMarblesNew(2,120,420,6)
createMarblesNew(2,60,360,8)
createMarblesNew(2,60,300,4)
createMarblesNew(2,300,300,4)

DISPLAYSURF.fill(WHITE)
# Beginning Game Loop
#isClicked = False
class clickers():
    def __init__(self):
        super().__init__()
        self.isClicked = False

booleo = clickers()
while True:
    pygame.display.update()
    for item in list:
        item.updates()
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not booleo.isClicked:
            for item in list:
                if item.rect.collidepoint(event.pos):
                    if item.isMarble:
                        item.clicked = not item.clicked
                        booleo.isClicked = not booleo.isClicked
                        
        elif event.type == pygame.MOUSEBUTTONDOWN and booleo.isClicked:
            newLocX = 1 
            newLocY = 1
            for item2 in list:
                if not item2.isMarble and item2.rect.collidepoint(event.pos) and item2.isValidSpot:      
                    newLocX = item2.getX()
                    newLocY = item2.getY()
                    
                    for item3 in list:
                        
                        
                        if item3.isMarble and item3.clicked and item2.isValidSpot:
                            if item3.validMove(newLocX,newLocY):
                                var = item3.whichDelete(newLocX,newLocY)
                                item3.setPosition(newLocX,newLocY)                                
                                item3.clicked = not item3.clicked
                                
                                booleo.isClicked = not booleo.isClicked
                                
                                for items in list:
                                    if items.id == var and items.isMarble:
                                        items.setPosition(50,50)

                            


   
    FramePerSec.tick(FPS)