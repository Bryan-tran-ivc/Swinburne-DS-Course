import pygame as pg

from entity import Entity
from const import *


class Goombas(Entity):
    # This class handles the basic Goomba enemy behavior
    def __init__(self, x_pos, y_pos, move_direction):
        super().__init__()
        # Set the Goomba's hitbox to a standard 32x32 square
        self.rect = pg.Rect(x_pos, y_pos, 32, 32)

        # Set move direction: Right if True (1), Left if False (-1)
        if move_direction:
            self.x_vel = 1
        else:
            self.x_vel = -1

        self.crushed = False
        self.current_image = 0
        self.image_tick = 0
        
        # Load walking frames and death frames
        self.images = [
            pg.image.load('images/goombas_0.png').convert_alpha(),    # Walk 1
            pg.image.load('images/goombas_1.png').convert_alpha(),    # Walk 2
            pg.image.load('images/goombas_dead.png').convert_alpha()  # Flat (crushed)
        ]
        # Add an upside-down frame for when the Goomba is hit by a shell
        self.images.append(pg.transform.flip(self.images[0], 0, 180))

    def die(self, core, instantly, crushed):
        # Handle the Goomba being removed from the game
        if not instantly:
            # Award points and show score text on screen
            core.get_map().get_player().add_score(core.get_map().score_for_killing_mob)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y)

            if crushed:
                # If Mario jumped on it, play squash sound and set flat image
                self.crushed = True
                self.image_tick = 0
                self.current_image = 2
                self.state = -1
                core.get_sound().play('kill_mob', 0, 0.5)
                self.collision = False # Turn off collision so it doesn't hurt Mario anymore

            else:
                # If hit by a shell, pop it up into the air upside down
                self.y_vel = -4
                self.current_image = 3
                core.get_sound().play('shot', 0, 0.5)
                self.state = -1
                self.collision = False

        else:
            # Remove immediately if needed
            core.get_map().get_mobs().remove(self)

    def check_collision_with_player(self, core):
        # Check if the Goomba touches Mario
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if self.state != -1:
                    # If Mario is falling, he kills the Goomba
                    if core.get_map().get_player().y_vel > 0:
                        self.die(core, instantly=False, crushed=True)
                        core.get_map().get_player().reset_jump()
                        core.get_map().get_player().jump_on_mob()
                    else:
                        # If Mario walks into it from the side, Mario gets hurt
                        if not core.get_map().get_player().unkillable:
                            core.get_map().get_player().set_powerlvl(0, core)

    def update_image(self):
        # Switch walking frames every 14 ticks to create animation
        self.image_tick += 1
        if self.image_tick == 14:
            self.current_image = 1
        elif self.image_tick == 28:
            self.current_image = 0
            self.image_tick = 0

    def update(self, core):
        # State 0: Normal walking
        if self.state == 0:
            self.update_image()

            # Apply gravity if the Goomba walks off a ledge
            if not self.on_ground:
                self.y_vel += GRAVITY

            # Handle wall and floor collisions
            blocks = core.get_map().get_blocks_for_collision(int(self.rect.x // 32), int(self.rect.y // 32))
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            # Check if Goomba fell off the map
            self.check_map_borders(core)

        # State -1: Dying
        elif self.state == -1:
            if self.crushed:
                # Let the crushed flat image stay on screen for a short time before disappearing
                self.image_tick += 1
                if self.image_tick == 50:
                    core.get_map().get_mobs().remove(self)
            else:
                # If popped up, let it fall through the floor off-screen
                self.y_vel += GRAVITY
                self.rect.y += self.y_vel
                self.check_map_borders(core)

    def render(self, core):
        # Draw the Goomba based on camera position
        core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))