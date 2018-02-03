#Pygame template - skeleton for a new py gmae project
import pygame
import random
from settings import * #import everything eg.no need for import.width


#iniitialise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game") #What will the window be called?
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
#Game loop
running = True
while running:
    #Runninf at the right speed
    clock.tick(fps)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
