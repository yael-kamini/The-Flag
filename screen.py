import time
import pygame
import consts
from consts import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, SOLDIER_IMG
from consts import GREEN

screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
color = GREEN
screen.fill(color)
pygame.display.flip()
time.sleep(4)


def show_img(soldier_img):
    self.image = pygame.image.load(SOLDIER_IMG)

# dark_screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
# dark_color = BLACK
# screen.fill(dark_color)
# pygame.display.flip()
# time.sleep(4)




def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)



