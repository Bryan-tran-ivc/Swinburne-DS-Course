import pygame as pg


class BGObject(object):
    # This class is for decorative background items like clouds, bushes, or hills
    def __init__(self, x, y, image):
        # Set the position and standard 32x32 size
        self.rect = pg.Rect(x, y, 32, 32)
        self.image = image
        # Mark as a background object so entities don't collide with it
        self.type = 'BGObject'

    def render(self, core):
        # Draw the object using the camera offset so it scrolls with the level
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))