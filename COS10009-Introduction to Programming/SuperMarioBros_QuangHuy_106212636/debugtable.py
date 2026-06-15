import pygame as pg


class DebugTable(object):
    # This class shows game data on screen to help with bug fixing
    def __init__(self):
        # Set up a small font and a semi-transparent black background
        self.font = pg.font.SysFont('Consolas', 12)
        self.darkArea = pg.Surface((200, 100)).convert_alpha()
        self.darkArea.fill((0, 0, 0, 200)) # Dark box behind the text
        self.text = []
        self.rect = 0
        self.offsetX = 12 # Space between lines of text
        self.x = 5
        self.mode = 2 # Setting to determine if debug is shown

    def update_text(self, core):
        # Only collect data if mode 2 is active
        if self.mode == 2:
            # Create a list of strings showing things like FPS, position, and power level
            self.text = [
                'FPS: ' + str(int(core.clock.get_fps())),
                'Rect: ' + str(core.get_map().get_player().rect.x) + ' ' + str(core.get_map().get_player().rect.y) + ' h: ' + str(core.get_map().get_player().rect.h),
                'g: ' + str(core.get_map().get_player().on_ground) + ' LVL: ' + str(core.get_map().get_player().powerLVL) + ' inv: ' + str(core.get_map().get_player().unkillable),
                'Spr: ' + str(core.get_map().get_player().spriteTick) + ' J lock: ' + str(core.get_map().get_player().already_jumped),
                'Up  : ' + str(core.get_map().get_player().inLevelUpAnimation) + '  time: ' + str(core.get_map().get_player().inLevelUpAnimationTime),
                'Down: ' + str(core.get_map().get_player().inLevelDownAnimation) + '  time: ' + str(core.get_map().get_player().inLevelDownAnimationTime),
                'Mobs: ' + str(len(core.get_map().get_mobs())) + ' Debris: ' + str(len(core.get_map().debris))
            ]

    def render(self, core):
        # Draw the debug box and each line of text onto the screen
        self.x = 105
        if self.mode == 2:
            core.screen.blit(self.darkArea, (0, 100)) # Draw background box
            for string in self.text:
                # Turn the string into an image and draw it
                self.rect = self.font.render(string, True, (255, 255, 255))
                core.screen.blit(self.rect, (5, self.x))
                self.x += self.offsetX # Move down for the next line