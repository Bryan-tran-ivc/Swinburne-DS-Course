import pygame as pg


class Flag(object):
    # This class handles the flagpole at the end of the level
    def __init__(self, x_pos, y_pos):
        self.rect = None

        # Variables to track the flag sliding down
        self.flag_offset = 0
        self.flag_omitted = False

        # The flag consists of two parts: the tall pillar and the moving flag piece
        self.pillar_image = pg.image.load('images/flag_pillar.png').convert_alpha()
        self.pillar_rect = pg.Rect(x_pos + 8, y_pos, 16, 304) # Hitbox for the pole

        self.flag_image = pg.image.load('images/flag.png').convert_alpha()
        self.flag_rect = pg.Rect(x_pos - 18, y_pos + 16, 32, 32) # Hitbox for the flag piece

    def move_flag_down(self):
        # Move the flag piece down the pole
        self.flag_offset += 3
        self.flag_rect.y += 3

        # Stop moving once it reaches the bottom of the pole
        if self.flag_offset >= 255:
            self.flag_omitted = True

    def render(self, core):
        # Draw the pillar first using the camera offset
        self.rect = self.pillar_rect
        core.screen.blit(self.pillar_image, core.get_map().get_camera().apply(self))

        # Draw the flag piece second so it appears on top of the pillar
        self.rect = self.flag_rect
        core.screen.blit(self.flag_image, core.get_map().get_camera().apply(self))