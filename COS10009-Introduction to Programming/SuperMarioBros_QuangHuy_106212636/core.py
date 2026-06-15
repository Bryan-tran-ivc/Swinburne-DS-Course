from os import environ

import pygame as pg
from pygame.locals import *

from const import *
from map import Map
from menumanager import MenuManager
from sound import Sound


class Core(object):
    # This is the heart of the game that ties everything together
    def __init__(self):
        # Center the window and set up the audio mixer
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Mario by S&D')
        
        # Set up the window and the game clock
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        # Initialize the world map, sound engine, and menu system
        self.oWorld = Map('1-1')
        self.oSound = Sound()
        self.oMM = MenuManager(self)

        # Variables to track which keys are currently being pressed
        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyEnter = False

    def main_loop(self):
        # The main game loop: get input, update physics, and draw everything
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS) # Keep the game running at a steady speed

    def input(self):
        # Choose which input logic to use based on the current screen
        if self.get_mm().currentGameState == 'Game':
            self.input_player()
        else:
            self.input_menu()

    def input_player(self):
        # Handle keyboard events while the game is actually being played
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            # When a key is pressed down, set the variable to True
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.keyR = True
                elif e.key == K_LEFT:
                    self.keyL = True
                elif e.key == K_DOWN:
                    self.keyD = True
                elif e.key == K_UP:
                    self.keyU = True
                elif e.key == K_RETURN:
                    self.keyEnter = True

            # When a key is released, set the variable back to False
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.keyR = False
                elif e.key == K_LEFT:
                    self.keyL = False
                elif e.key == K_DOWN:
                    self.keyD = False
                elif e.key == K_UP:
                    self.keyU = False
                elif e.key == K_RETURN:
                    self.keyEnter = False

    def input_menu(self):
        # Handle keyboard events for the Menu or Leaderboard screens
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    # Pressing Enter on Main Menu starts the game immediately
                    if self.get_mm().currentGameState == 'MainMenu':
                        self.get_mm().start_loading(self)
                    # Pressing Enter on Leaderboard goes back to Menu
                    elif self.get_mm().currentGameState == 'Leaderboard':
                        self.get_mm().currentGameState = 'MainMenu'
                        self.get_map().reset(True)
                        self.get_mm().runs_tracker.clear_runs()

    def update(self):
        # Tell the menu manager to update the logic for the current state
        self.get_mm().update(self)

    def render(self):
        # Tell the menu manager to draw the current state to the screen
        self.get_mm().render(self)

    # Helper methods to easily access core components from other classes
    def get_map(self):
        return self.oWorld

    def get_mm(self):
        return self.oMM

    def get_sound(self):
        return self.oSound