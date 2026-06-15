import pygame as pg

from const import *


class Camera(object):
    # This class makes the screen follow Mario as he moves
    def __init__(self, width, height):
        # Create a rectangle representing the level size
        self.rect = pg.Rect(0, 0, width, height)
        self.complex_camera(self.rect)

    def complex_camera(self, target_rect):
        # Calculate X and Y to keep Mario in the center of the screen
        x, y = target_rect.x, target_rect.y
        width, height = self.rect.width, self.rect.height
        x, y = (-x + WINDOW_W / 2 - target_rect.width / 2), (-y + WINDOW_H / 2 - target_rect.height)

        # Stop the camera from scrolling past the map edges
        x = min(0, x)
        x = max(-(self.rect.width - WINDOW_W), x)
        y = WINDOW_H - self.rect.h

        return pg.Rect(x, y, width, height)

    def apply(self, target):
        # Adjust an object's position based on camera scroll
        return target.rect.x + self.rect.x, target.rect.y

    def update(self, target):
        # Move the camera to track the target (Mario)
        self.rect = self.complex_camera(target)

    def reset(self):
        # Reset camera to the start of the level
        self.rect = pg.Rect(0, 0, self.rect.w, self.rect.h)