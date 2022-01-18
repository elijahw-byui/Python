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
 
# Creating Lines and Shapes
def createMarbles(num1, num2):
    j = 0
    i = 0
    for j in range(num1,num2):
        
        for i in range(num1,num2):
            pygame.draw.circle(DISPLAYSURF, BLUE, ((i*80), (j*80)), 30)



 
# Beginning Game Loop
createMarbles(1,7)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)