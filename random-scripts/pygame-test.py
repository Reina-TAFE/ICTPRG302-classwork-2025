import substitution
import pygame
from pygame.locals import *
import pygame.freetype
import Funk

pygame.init()


SCREEN_WIDTH = 950
SCREEN_HEIGHT = 400
FONT = pygame.font.SysFont('Arial', size=24)

alphabet = substitution.get_encrypted_alphabet()
message = substitution.get_random_message()
cipher_message = substitution.encrypt_message(message, alphabet)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Decryptle")

screen.fill((255, 255, 255))
# pygame.draw.rect(screen, (64, 64, 128), (150, 100, 600, 100), 0)

def draw_table(table_data):
    cell_height = 40
    cell_width = 30
    row_1 = list(table_data.keys())
    row_2 = list(table_data.values())
    # row_1 = "  |  ".join(list(table_data.keys()))
    # row_2 = "  |  ".join(list(table_data.values()))

    for row in range(3):
        pygame.draw.line(screen, (0,0,0),(120, row * cell_height), (26* cell_width + 120, row * cell_height))
    for col in range(27):
        pygame.draw.line(screen, (0,0,0), (col * cell_width + 120, 0), (col * cell_width + 120, 2 * cell_height))
    header1 = FONT.render("Encrypted", True, (0,0,0))
    header2 = FONT.render("Decrypted", True, (0,0,0))
    screen.blit(header1, (10, cell_width // 4))
    screen.blit(header2, (10, cell_width * 6 // 4))

    for i in range(26):
        letter1 = FONT.render(row_1[i], True, (0,0,0))
        letter2 = FONT.render(row_2[i], True, (0,0,0))
        screen.blit(letter1, ( (i + 1) * cell_width +100, cell_height // 5))
        screen.blit(letter2, ((i + 1) * cell_width +100, cell_height * 6 // 5))


# screen = pygame.display.set_mode([600, 600])
def draw_cipher_text(cipher_text):
    draw_message = FONT.render(cipher_text, True, (0,0,0))
    screen.blit(draw_message, (SCREEN_WIDTH // 2, 120))


draw_table(alphabet)
draw_cipher_text(cipher_message)
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
pygame.quit()