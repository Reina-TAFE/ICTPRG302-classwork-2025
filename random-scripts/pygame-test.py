# import substitution
import pygame
from pygame.locals import *

pygame.init()
run = True
while run:


    # screen = pygame.display.set_mode([600, 600])
    clock = pygame.time.Clock()

    window = pygame.display.set_mode([600, 600])
    bg_colour = (64, 64, 128)

    window.fill((255, 255, 255))

    pygame.draw.rect(window, (64, 64, 128), (100, 100, 400, 100), 0)
pygame.display.update()