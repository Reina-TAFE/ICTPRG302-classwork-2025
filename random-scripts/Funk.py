from typing import Any, List, Optional, Sequence, Tuple, Union, overload
from pygame._common import ColorValue, Coordinate, Literal, RectValue, RGBAOutput
import pygame


def text_to_screen(screen, text, x, y, size=50,
                   color=(200, 000, 000), font_type='data/fonts/orecrusherexpand.ttf'):
    try:

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print('Font Error, saw it coming')
        raise e


def center_element(self,
                   surface_size: Tuple,
                   element_size: Tuple,
                   surface_position: Optional[Tuple]
                   ) -> Tuple[float, float]:
    if surface_position:
        center_x = surface_position[0] + float((surface_size[0] - element_size[0]) / 2)
        center_y = surface_position[1] + float((surface_size[1]-element_size[1]) / 2)
        center_pos = (center_x, center_y)
    else:
        center_pos = float((surface_size[0] - element_size[0]) / 2), float((surface_size[1]-element_size[1]) / 2)
    return center_pos

