import pygame, sys
from pygame.locals import *


 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 1
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

class Marble(pygame.sprite.Sprite):
    id = (0,0)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/elijah/Desktop/CSE310/Python Module/PyProject/Assets/Poorman.png")
        self.rect = self.image.get_rect()
    def setPosition(self, num1, num2):
        self.rect.center = (num1,num2) 
        self.id = (num1, num2)
    def updates(self):
        co1 = self.id[0]
        co2 = self.id[1]
        self.draw(DISPLAYSURF,co1, co2)
        #self.setPosition()
    def drawMarble(self, num1, num2):
        pygame.draw.circle(DISPLAYSURF, BLUE, (num1,num2), 30)
    def moveMarble(self, num3, num4):
        self.position = pygame.mouse.get_pos
    def draw(self, surface,num3,num4):
        self.setPosition(num3, num4)
        surface.blit(self.image, self.rect) 


# Creating Marbles
def createMarbles(num1, num2):
    j = 0
    i = 0
    for j in range(num1,num2):
        
        for i in range(num1,num2):
            newi = (i * 80)
            newj = (j * 80)
            #pygame.draw.circle(DISPLAYSURF, BLUE, ((i*80), (j*80)), 30)
            marble = Marble()
            list.append(marble)
            #marble.drawMarble(newi, newj)
            marble.draw(DISPLAYSURF, newi, newj)


# Beginning Game Loop
createMarbles(1,7)
for item in list:
    print (item.id)
DISPLAYSURF.fill(WHITE)

while True:
    pygame.display.update()
    for item in list:
        item.updates()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    FramePerSec.tick(FPS)