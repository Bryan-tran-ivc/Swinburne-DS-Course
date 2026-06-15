import pygame as pg

from const import *
from text import Text


class LoadingMenu(object):
    # This class handles the black loading screen between the menu and the level
    def __init__(self, core):
        self.iTime = pg.time.get_ticks()
        self.loadingType = True  # True means loading into game, False means Game Over/Menu
        self.bg = pg.Surface((WINDOW_W, WINDOW_H)) # Black background
        self.text = Text('WORLD ' + core.oWorld.get_name(), 32, (WINDOW_W / 2, WINDOW_H / 2))

    def update(self, core):
        # Wait for a few seconds before switching screens
        if pg.time.get_ticks() >= self.iTime + (5250 if not self.loadingType else 2500):
            if self.loadingType:
                # Start the game and play music
                core.oMM.currentGameState = 'Game'
                core.get_sound().play('overworld', 999999, 0.5)
                core.get_map().in_event = False
            else:
                # Go back to the main menu
                core.oMM.currentGameState = 'MainMenu'
                self.set_text_and_type('WORLD ' + core.oWorld.get_name(), True)
                core.get_map().reset(True)

    def set_text_and_type(self, text, type):
        # Update the screen text (like "GAME OVER") and the loading mode
        self.text = Text(text, 32, (WINDOW_W / 2, WINDOW_H / 2))
        self.loadingType = type

    def render(self, core):
        # Draw the black background and the text
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

    def update_time(self):
        # Reset the timer so the loading screen stays for the full duration
        self.iTime = pg.time.get_ticks()