import pygame as pg

from entity import Entity
from const import *


class Mushroom(Entity):
    def __init__(self, x_pos, y_pos, move_direction):
        super().__init__()
        # Set hitbox and initial position
        self.rect = pg.Rect(x_pos, y_pos, 32, 32)

        # Set move direction (right or left)
        if move_direction:
            self.x_vel = 1
        else:
            self.x_vel = -1

        # Spawn state variables
        self.spawned = False
        self.spawn_y_offset = 0
        self.image = pg.image.load('images/mushroom.png').convert_alpha()

    def check_collision_with_player(self, core):
        # Give player power-up and remove mushroom on touch
        if self.rect.colliderect(core.get_map().get_player().rect):
            core.get_map().get_player().set_powerlvl(1, core)
            core.get_map().get_mobs().remove(self)

    def die(self, core, instantly, crushed):
        # Remove mushroom from the game
        core.get_map().get_mobs().remove(self)

    def spawn_animation(self):
        # Slide mushroom up out of the block
        self.spawn_y_offset -= 1
        self.rect.y -= 1

        # Finish animation after moving 32 pixels
        if self.spawn_y_offset == - 32:
            self.spawned = True

    def update(self, core):
        if self.spawned:
            # Apply gravity and handle collisions
            if not self.on_ground:
                self.y_vel += GRAVITY

            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            # Check if mushroom falls out of map
            self.check_map_borders(core)
        else:
            # Continue spawning
            self.spawn_animation()

    def render(self, core):
        # Draw mushroom relative to camera
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))