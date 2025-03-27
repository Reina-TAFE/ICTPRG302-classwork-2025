import substitution
import pygame
from pygame.locals import *
import pygame.freetype
import Funk

pygame.init()
run = True

text_font = pygame.freetype.SysFont('freesansbold.ttf', size=20)

alphabet = substitution.get_encrypted_alphabet()
clock = pygame.time.Clock()

window = pygame.display.set_mode([900, 600])

window.fill((255, 255, 255))
pygame.draw.rect(window, (64, 64, 128), (150, 100, 600, 100), 0)

def draw_table(table_data):
    row_1 = "  |  ".join(list(table_data.keys()))
    row_2 = "  |  ".join(list(table_data.values()))
    table_bg = pygame.Rect(150, 100, 300, 150)
    pygame.draw.rect(window, (64, 64, 128), table_bg, 0)
    Funk.text_to_screen(window, row_1, row_2, text_font)


# screen = pygame.display.set_mode([600, 600])

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    draw_table(alphabet)
    pygame.display.update()
pygame.quit()