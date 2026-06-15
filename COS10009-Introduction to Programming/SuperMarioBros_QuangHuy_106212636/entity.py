import pygame as pg
from const import *


class Entity(object):
    # This is a base class for everything that moves (enemies, power-ups, etc.)
    def __init__(self):

        self.state = 0
        self.x_vel = 0
        self.y_vel = 0

        self.move_direction = True
        self.on_ground = False
        self.collision = True

        self.image = None
        self.rect = None

    def update_x_pos(self, blocks):
        # Move horizontally and check for wall collisions
        self.rect.x += self.x_vel

        for block in blocks:
            # Ignore background objects; only collide with solid blocks
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    # If hitting a wall, bounce back in the opposite direction
                    if self.x_vel > 0:
                        self.rect.right = block.rect.left
                        self.x_vel = - self.x_vel
                    elif self.x_vel < 0:
                        self.rect.left = block.rect.right
                        self.x_vel = - self.x_vel

    def update_y_pos(self, blocks):
        # Move vertically based on falling speed
        self.rect.y += self.y_vel * FALL_MULTIPLIER

        self.on_ground = False
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    # If falling and hitting the top of a block, stop and stand on it
                    if self.y_vel > 0:
                        self.on_ground = True
                        self.rect.bottom = block.rect.top
                        self.y_vel = 0

    def check_map_borders(self, core):
        # Kill the entity if it falls into a pit
        if self.rect.y >= 448:
            self.die(core, True, False)
        
        # Prevent the entity from walking off the left side of the map
        if self.rect.x <= 1 and self.x_vel < 0:
            self.x_vel = - self.x_vel

    def die(self, core, instantly, crushed):
        # Placeholder function to be filled in by child classes (like Goomba or Mushroom)
        pass

    def render(self, core):
        # Placeholder for drawing the entity on screen
        pass