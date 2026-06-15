import pygame as pg


class CoinDebris(object):
    # This class handles the coin that pops out when you hit a question block
    def __init__(self, x_pos, y_pos):
        # Set the starting position and size of the coin
        self.rect = pg.Rect(x_pos, y_pos, 16, 28)

        # Movement variables for the "jump" effect
        self.y_vel = -2
        self.y_offset = 0
        self.moving_up = True

        # Animation variables
        self.current_image = 0
        self.image_tick = 0
        # Load the spinning coin frames
        self.images = [
            pg.image.load('images/coin_an0.png').convert_alpha(),
            pg.image.load('images/coin_an1.png').convert_alpha(),
            pg.image.load('images/coin_an2.png').convert_alpha(),
            pg.image.load('images/coin_an3.png').convert_alpha()
        ]

    def update(self, core):
        # Update the animation frame every 15 ticks
        self.image_tick += 1

        if self.image_tick % 15 == 0:
            self.current_image += 1

        # Reset animation loop
        if self.current_image == 4:
            self.current_image = 0
            self.image_tick = 0

        # Move the coin up until it reaches a certain height
        if self.moving_up:
            self.y_offset += self.y_vel
            self.rect.y += self.y_vel
            if self.y_offset < -50: # After rising 50 pixels, start falling
                self.moving_up = False
                self.y_vel = -self.y_vel # Reverse velocity to fall down
        else:
            # Move the coin back down
            self.y_offset += self.y_vel
            self.rect.y += self.y_vel
            # Once it returns to the starting height, remove it from the game
            if self.y_offset == 0:
                core.get_map().debris.remove(self)

    def render(self, core):
        # Draw the current spinning frame with the camera offset applied
        core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))