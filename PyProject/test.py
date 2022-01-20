from typing import SupportsComplex
import pygame, sys
from pygame.locals import *


 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
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
    def setPosition(self, num1, num2):
        self.rect.center = (num1,num2) 
        self.id = (num1, num2)
    def updates(self):
        co1 = self.id[0]
        co2 = self.id[1]
        self.draw(DISPLAYSURF,co1, co2)
    def draw(self, surface,num3,num4):
        self.setPosition(num3, num4)
        surface.blit(self.image, self.rect) 

class Marble(pygame.sprite.Sprite):
    id = (0,0)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Poorman.png")
        self.rect = self.image.get_rect()
        self.clicked = False
        self.isMarble = True
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
 
    def drawMarble(self, num1, num2):
        pygame.draw.circle(DISPLAYSURF, BLUE, (num1,num2), 30)
    def moveMarble(self, num3, num4):
        self.position = pygame.mouse.get_pos
    def draw(self, surface,num3,num4):
        self.setPosition(num3, num4)
        surface.blit(self.image, self.rect) 
    def resetPosition(self):
        pass


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

def isMarbleSelected(list):
    for item in list:
        if item.isMarble:
            if item.clicked:
                return True
            else:
                return False

for item in list:
    print (item.id)
DISPLAYSURF.fill(WHITE)
# Beginning Game Loop
isClicked= False
while True:
    pygame.display.update()
    #isClicked = False
    for item in list:
        item.updates()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if isMarbleSelected(list):
        if event.type == pygame.MOUSEBUTTONDOWN and not isClicked:
            for item in list:
                if item.rect.collidepoint(event.pos):
                    print(event.pos)
                    if item.isMarble:
                        item.clicked = not item.clicked
                        isClicked = True
                        if item.clicked:
                            print(item.clicked)
                            #item.setPosition(50,50)
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked:
            for item in list:
                if item.isMarble and item.clicked:
                    var = event.pos[0]
                    var1 = event.pos[1]
                    item.setPosition(var, var1)
                    item.clicked = not item.clicked
                    isClicked = False




   
    FramePerSec.tick(FPS)