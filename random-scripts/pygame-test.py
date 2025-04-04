import substitution
import pygame
from pygame.locals import *
import pygame.freetype
import re
import Funk

pygame.init()


SCREEN_WIDTH = 950
SCREEN_HEIGHT = 400
FONT = pygame.font.SysFont('Arial', size=24)

alphabet = substitution.get_encrypted_alphabet()
message, url = substitution.get_random_message()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Decryptle")

SCREEN.fill((255, 255, 255))
class RefTable(object):
    def __init__(self, x, y, w, h, data):
        self.rect = pygame.Rect(x, y, w, h)
        self.table_data = data
        self.cell_width = (w - 120) / 26
        self.cell_height = h / 2

    def draw_table(self):
        # Create Rows (PyGame)
        row_1 = list(self.table_data.keys())
        row_2 = list(self.table_data.values())

        # Draw Lines For Table
        for row in range(3):
            pygame.draw.line(SCREEN, (0,0,0),(120, row * self.cell_height), (26* self.cell_width + 120, row * self.cell_height))
        for col in range(27):
            pygame.draw.line(SCREEN, (0,0,0), (col * self.cell_width + 120, 0), (col * self.cell_width + 120, 2 * self.cell_height))

        # Draw Headers For Table Rows
        header_row_1 = FONT.render("Encrypted", True, (0,0,0))
        header_row_2 = FONT.render("Decrypted", True, (0,0,0))

        # Blit Row Headers to SCREEN
        SCREEN.blit(header_row_1, (10, self.cell_width // 4))
        SCREEN.blit(header_row_2, (10, self.cell_width * 6 // 4))

        # Draw Letters to table and blit
        for i in range(26):
            letter1 = FONT.render(row_1[i], True, (0,0,0))
            letter2 = FONT.render(row_2[i], True, (0,0,0))
            SCREEN.blit(letter1, ( (i + 1) * self.cell_width +100, self.cell_height // 5))
            SCREEN.blit(letter2, ((i + 1) * self.cell_width +100, self.cell_height * 6 // 5))

    def update(self, new_data):
        self.table_data = new_data
        pygame.display.flip()
        self.draw_table()

class InputBox:
    COLOUR_INACTIVE = (0, 128, 255)
    COLOUR_ACTIVE = (0, 74, 148)

    def __init__(self, target, x, y, w, h, text='a'):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.colour = InputBox.COLOUR_INACTIVE
        self.txt_surface = FONT.render(self.text, True, (0,0,0))
        self.active = False
        self.target = target

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.colour = InputBox.COLOUR_ACTIVE if self.active else InputBox.COLOUR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.handle_guess()
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.colour)

    def handle_guess(self):
        user_guess = self.text
        if re.match(r'[a-zA-Z]=[a-zA-Z]', user_guess):
            guess = user_guess.strip().split('=')
            self.target.update(guess)
        else:
            print("Invalid Substitution")

    def draw(self, screen):
        SCREEN.blit(self.txt_surface, (self.rect.x + (self.rect.w /3), self.rect.y + (self.rect.h / 3)))
        input_rect = self.txt_surface.get_rect(center=(SCREEN_WIDTH / 2, 2 * SCREEN_HEIGHT / 3))
        pygame.draw.rect(SCREEN, self.colour, self.rect, 0)

class CipherText(object):
    def __init__(self, text, keys, ref):
        self.surface = pygame.Surface([650, 200])
        self.surface.fill((235,235,235))
        self.origin = text
        self.ref = ref
        self.keys = keys
        user_keys = list(keys.values())
        user_starting_values = user_keys
        self.user_dict = dict(zip(user_keys, user_starting_values))
        self.cipher_text = self.encrypt(init=True)

    # Encrypt text
    def encrypt(self, init=False):
        cipher_message = ''
        if init:
            for letter in self.origin:

                if letter.isalpha():
                    if letter.isupper():
                        cipher_message = cipher_message + self.keys[letter.lower()].upper()
                    else:
                        cipher_message = cipher_message + self.keys[letter]
                else:
                    cipher_message = cipher_message + letter
        else:
            for letter in self.cipher_text:

                if letter.isalpha():
                    if letter.isupper():
                        cipher_message = cipher_message + self.user_dict[letter.lower()].upper()
                    else:
                        cipher_message = cipher_message + self.user_dict[letter]
                else:
                    cipher_message = cipher_message + letter
        return cipher_message

    # Update keys with new keys
    def update(self, new_keys):
        self.keys[new_keys[0]] = new_keys[1]
        self.cipher_text = self.encrypt()
        self.ref.update(self.keys)

    # Draw Cipher Text
    # def draw_cipher_text(self):
    #     draw_message = FONT.render(self.cipher_text, True, (0,0,0))
    #     text_rect = draw_message.get_rect(center=(SCREEN_WIDTH / 2, 120))
    #     SCREEN.blit(draw_message, text_rect)

    def draw_text(self, aa=False, bkg=None):
        SCREEN.blit(self.surface, (100, 120))
        rect = self.surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        text = self.cipher_text
        y = rect.top
        line_spacing = -2
        # self.surface.fill((255, 255, 255), rect=rect)

        # get the height of the font
        font_height = FONT.size("Tg")[1]

        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + font_height > rect.bottom:
                break

            # determine maximum width of line
            while FONT.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # n = text.rfind("\n", 0, i) + 1
            # if FONT.size(text[:n])[0] < rect.width and FONT.size(text[:n])[0] < FONT.size(text[:i])[0]:
            #     image = FONT.render(text[:n], aa, (0, 0, 0))
            #     SCREEN.blit(image, (rect.left, y))
            #     y += font_height + line_spacing
            #     text = text[n:]
            #     continue

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = FONT.render(text[:i], 1, (0,0,0), bkg)
                image.set_colorkey(bkg)
            else:
                image = FONT.render(text[:i], aa, (0,0,0))

            SCREEN.blit(image, (rect.left, y))
            y += font_height + line_spacing

            # remove the text we just blitted
            text = text[i:]


def play_pygame():
    ref_table = RefTable(50, 20, 780, 80, alphabet)
    ref_table.draw_table()
    cipher = CipherText(message, alphabet, ref_table)
    cipher.draw_text()
    input_box = InputBox(cipher, 50, 100, 60, 80)
    input_box.draw(SCREEN)

    # pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            else:
                input_box.handle_event(event)
        pygame.display.update()
    pygame.quit()

play_pygame()
