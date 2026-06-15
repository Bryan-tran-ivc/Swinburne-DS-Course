import pygame as pg

from entity import Entity
from const import *


class Koopa(Entity):
    # This class handles the Koopa enemy, including its shell states
    def __init__(self, x_pos, y_pos, move_direction):
        super().__init__()
        # Initial taller hitbox for the standing turtle
        self.rect = pg.Rect(x_pos, y_pos, 32, 46)

        self.move_direction = move_direction

        # Set speed based on starting direction (Right: 1, Left: -1)
        if move_direction:
            self.x_vel = 1
        else:
            self.x_vel = -1

        self.current_image = 0
        self.image_tick = 0
        # 0 & 1: Walk frames, 2: Shell frame
        self.images = [
            pg.image.load('images/koopa_0.png').convert_alpha(),
            pg.image.load('images/koopa_1.png').convert_alpha(),
            pg.image.load('images/koopa_dead.png').convert_alpha()
        ]
        # Add flipped images for moving right and upside down for death
        self.images.append(pg.transform.flip(self.images[0], 180, 0))
        self.images.append(pg.transform.flip(self.images[1], 180, 0))
        self.images.append(pg.transform.flip(self.images[2], 0, 180))

    # Note on states: 0 = Walking, 1 = Inside shell, 2 = Sliding shell, -1 = Dead

    def check_collision_with_player(self, core):
        # Handle interaction when Mario touches the Koopa
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if self.state != -1:
                    # If Mario jumps on top, trigger shell state
                    if core.get_map().get_player().y_vel > 0:
                        self.change_state(core)
                        core.get_sound().play('kill_mob', 0, 0.5)
                        core.get_map().get_player().reset_jump()
                        core.get_map().get_player().jump_on_mob()
                    else:
                        # If Mario hits from the side, damage him (unless he is invincible)
                        if not core.get_map().get_player().unkillable:
                            core.get_map().get_player().set_powerlvl(0, core)

    def check_collision_with_mobs(self, core):
        # Sliding shells kill other enemies they run into
        for mob in core.get_map().get_mobs():
            if mob is not self:
                if self.rect.colliderect(mob.rect):
                    if mob.collision:
                        mob.die(core, instantly=False, crushed=False)

    def die(self, core, instantly, crushed):
        # Remove Koopa or play falling-off-screen death animation
        if not instantly:
            core.get_map().get_player().add_score(core.get_map().score_for_killing_mob)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y)
            self.state = -1
            self.y_vel = -4 # Pop upward
            self.current_image = 5 # Upside down shell
        else:
            core.get_map().get_mobs().remove(self)

    def change_state(self, core):
        # Progresses the Koopa through shell logic
        self.state += 1
        self.current_image = 2

        # State transition: Walking --> Shell
        if self.rect.h == 46:
            self.x_vel = 0
            self.rect.h = 32 # Hitbox becomes shorter
            self.rect.y += 14 # Adjust position for shorter height
            core.get_map().get_player().add_score(100)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=100)

        # State transition: Still shell --> Sliding shell
        elif self.state == 2:
            core.get_map().get_player().add_score(100)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=100)

            # Kick shell away from player's current position
            if core.get_map().get_player().rect.x - self.rect.x <= 0:
                self.x_vel = 6
            else:
                self.x_vel = -6

        # State transition: If already sliding and hit again, it dies
        elif self.state == 3:
            self.die(core, instantly=False, crushed=False)

    def update_image(self):
        # Switch walking frames based on speed and time
        self.image_tick += 1

        if self.x_vel > 0:
            self.move_direction = True
        else:
            self.move_direction = False

        if self.image_tick == 35:
            self.current_image = 4 if self.move_direction else 1
        elif self.image_tick == 70:
            self.current_image = 3 if self.move_direction else 0
            self.image_tick = 0

    def update(self, core):
        # Update behavior based on current behavior state
        if self.state == 0: # Walking
            self.update_image()
            if not self.on_ground:
                self.y_vel += GRAVITY
            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, (self.rect.y - 14) // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)
            self.check_map_borders(core)

        elif self.state == 1: # Still Shell
            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)
            self.check_map_borders(core)

        elif self.state == 2: # Sliding Shell
            if not self.on_ground:
                self.y_vel += GRAVITY
            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)
            self.check_map_borders(core)
            self.check_collision_with_mobs(core) # Kill enemies hit by shell

        elif self.state == -1: # Death Animation
            self.rect.y += self.y_vel
            self.y_vel += GRAVITY
            self.check_map_borders(core)

    def render(self, core):
        # Draw current frame with camera offset applied
        core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))