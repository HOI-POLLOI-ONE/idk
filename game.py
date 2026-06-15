import sys

import pygame

pygame.init()                  #initializes all imported pyg modules.. very imp to call before useing any other pyg function 

screen=pygame.display.set_mode((800, 600))       #display surface/window

pygame.display.set_caption("spyr;nter")
clock=pygame.time.Clock()

running=True
 
while running:                        #gameloop
    for event in pygame.event.get():  # input events
        if event.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()              #system exit or application exit

    screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)                   #frame/second limit

                   











