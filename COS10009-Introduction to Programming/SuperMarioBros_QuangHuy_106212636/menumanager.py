import pygame as pg

from loadingmenu import LoadingMenu
from mainmenu import MainMenu
from leaderboardscreen import LeaderboardScreen
from leaderboard import RunsTracker


class MenuManager(object):
    # This class manages switching between different screens like the Menu or the Game
    def __init__(self, core):
        # Set the starting screen to the Main Menu
        self.currentGameState = 'MainMenu'

        # Initialize the different menu objects
        self.oMainMenu = MainMenu()
        self.oLoadingMenu = LoadingMenu(core)
        self.oLeaderboardScreen = None
        self.runs_tracker = RunsTracker()  # Keeps track of high scores

    def update(self, core):
        # Update logic based on which screen is currently active
        if self.currentGameState == 'MainMenu':
            pass

        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.update(core)

        elif self.currentGameState == 'Leaderboard':
            self.oLeaderboardScreen.update(core)
            self.oLeaderboardScreen.handle_input(core)

        elif self.currentGameState == 'Game':
            # Run the actual level logic
            core.get_map().update(core)

    def render(self, core):
        # Draw the appropriate graphics for the current screen
        if self.currentGameState == 'MainMenu':
            core.get_map().render_map(core)
            self.oMainMenu.render(core)

        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.render(core)

        elif self.currentGameState == 'Leaderboard':
            self.oLeaderboardScreen.render(core)

        elif self.currentGameState == 'Game':
            # Draw the game world and the UI (score, coins, etc.)
            core.get_map().render(core)
            core.get_map().get_ui().render(core)

        # Refresh the display to show the new frame
        pg.display.update()

    def start_loading(self, core):
        # Start the game immediately without showing the black loading screen
        self.currentGameState = 'Game'
        core.get_map().reset(True)
        core.get_map().in_event = False
        core.get_sound().play('overworld', 999999, 0.5)

    def show_leaderboard(self, core):
        # Create the leaderboard screen and switch to it
        self.oLeaderboardScreen = LeaderboardScreen(core, self.runs_tracker)
        self.currentGameState = 'Leaderboard'