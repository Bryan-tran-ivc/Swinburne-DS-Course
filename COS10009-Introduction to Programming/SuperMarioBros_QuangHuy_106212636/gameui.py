import pygame as pg


class GameUI(object):
    # This class draws the heads-up display (HUD) at the top of the screen
    def __init__(self):
        # Load the retro-style font and define the column headers
        self.font = pg.font.Font('fonts/emulogic.ttf', 20)
        self.text = 'SCORE COINS WORLD TIME LIVES'

    def render(self, core):
        # Draw the static labels (headers) across the top
        x = 10
        for word in self.text.split(' '):
            rect = self.font.render(word, False, (255, 255, 255))
            core.screen.blit(rect, (x, 0))
            x += 168 # Space out each word horizontally

        # Draw the player's current score below the 'SCORE' label
        text = self.font.render(str(core.get_map().get_player().score), False, (255, 255, 255))
        rect = text.get_rect(center=(60, 35))
        core.screen.blit(text, rect)

        # Draw the coin count below the 'COINS' label
        text = self.font.render(str(core.get_map().get_player().coins), False, (255, 255, 255))
        rect = text.get_rect(center=(230, 35))
        core.screen.blit(text, rect)

        # Draw the world name (e.g., "1-1") below the 'WORLD' label
        text = self.font.render(core.get_map().get_name(), False, (255, 255, 255))
        rect = text.get_rect(center=(395, 35))
        core.screen.blit(text, rect)

        # Draw the remaining level time below the 'TIME' label
        text = self.font.render(str(core.get_map().time), False, (255, 255, 255))
        rect = text.get_rect(center=(557, 35))
        core.screen.blit(text, rect)

        # Draw the remaining lives below the 'LIVES' label
        text = self.font.render(str(core.get_map().get_player().numOfLives), False, (255, 255, 255))
        rect = text.get_rect(center=(730, 35))
        core.screen.blit(text, rect)