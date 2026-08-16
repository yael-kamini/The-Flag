import random
import pygame

import consts

game_field = []

def create():
    global game_field
    game_field = [
        create_field_row(row, row_start=0, row_length=consts.BORED_COL)
        for row in
        range(consts.BORED_ROW)]


