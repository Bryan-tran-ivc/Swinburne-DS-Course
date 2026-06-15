import pygame as pg

from const import *


class PlatformDebris(object):
    # This class handles the little brick pieces that fly out when a block is broken
    def __init__(self, x_pos, y_pos):
        # Load the image for the small piece of debris
        self.image = pg.image.load('images/block_debris0.png').convert_alpha()

        # Create 4 separate rectangles for the 4 pieces of the block
        # They start at different spots around the original block's position
        self.rectangles = [
            pg.Rect(x_pos - 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos - 20, y_pos - 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos - 16, 16, 16)
        ]
        # Start with an upward velocity so they "pop" up before falling
        self.y_vel = -4
        self.rect = None

    def update(self, core):
        # Apply gravity so the pieces fall down over time
        self.y_vel += GRAVITY * FALL_MULTIPLIER

        # Loop through each of the 4 pieces to move them
        for i in range(len(self.rectangles)):
            # Update the vertical position based on velocity
            self.rectangles[i].y += self.y_vel
            # Make the first two pieces move left and the other two move right
            if i < 2:
                self.rectangles[i].x -= 1
            else:
                self.rectangles[i].x += 1

        # If the debris falls below the bottom of the map, delete it to keep the game fast
        if self.rectangles[1].y > core.get_map().mapSize[1] * 32:
            core.get_map().debris.remove(self)

    def render(self, core):
        # Draw each of the 4 pieces on the screen
        for rect in self.rectangles:
            # Set the current rectangle so the camera knows what to draw
            self.rect = rect
            # Draw the image adjusted for the camera's current position
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))