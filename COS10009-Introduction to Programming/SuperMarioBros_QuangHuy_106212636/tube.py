import pygame as pg

# Represents a pipe obstacle that crops its height based on its vertical position
class Tube(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # Load texture and calculate dimensions based on grid coordinates
        self.image = pg.image.load('images/tube.png').convert_alpha()
        length = (12 - y_pos) * 32
        
        # Crop the sprite and set its world position rect
        self.image = self.image.subsurface(0, 0, 64, length)
        self.rect = pg.Rect(x_pos * 32, y_pos * 32, 64, length)

    def render(self, core):
        # Draw the tube adjusted by the camera's current offset
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))