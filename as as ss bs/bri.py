import pygame
from pygame.locals import *
import ramdom

pygame.init()
# creat thw wind
widht=500
height=500
screen_size = (widht,height)
screen = pygame.display.set_mode(screen_size)
pygame.dislay.set_caption('car game')
 

#colors
gray = (100,100,100)
grenn = (76,208,56)
red = (208,0,0)
white = (255,255,255)
yellow = (255,232,0)

# game settings
gameover = False
speed=2
score = 0


#game top
clock = pygame.time.Clock()
fsp = 120
running = True
while running:

<clock.tick(fps)

for event in pygame.event.get():
    if event type0 == quit:
        running = False
    
    pygame.display.update()


    pygame.quit()