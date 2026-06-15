import pygame as pg

from const import *
from text import Text


class MainMenu(object):
    def __init__(self):
        # Load the main menu image and set up the "Press ENTER to start" text
        self.mainImage = pg.image.load("images/super_mario_bros.png").convert_alpha()

        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

    def render(self, core):
        # Draw the main menu image and the "Press ENTER to start" text on the screen. 
        # This function is called every frame while in the main menu state.
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
