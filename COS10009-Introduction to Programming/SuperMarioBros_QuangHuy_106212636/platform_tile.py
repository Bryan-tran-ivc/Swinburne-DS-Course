import pygame as pg


class Platform(object):
    def __init__(self, x, y, image, type_id):
        # position and image
        self.image = image
        self.rect = pg.Rect(x, y, 32, 32)

        # 22 = question block, 23 = brick block
        self.typeID = type_id
        self.type = 'Platform'

        # shaking effect
        self.shaking = False
        self.shakingUp = True
        self.shakeOffset = 0

        # only for question block
        if self.typeID == 22:
            self.currentImage = 0
            self.imageTick = 0
            self.isActivated = False
            self.bonus = 'coin'  # default bonus

    def update(self):
        # animate question block (change image)
        if self.typeID == 22:
            self.imageTick += 1
            if self.imageTick == 50:
                self.currentImage = 1
            elif self.imageTick == 60:
                self.currentImage = 2
            elif self.imageTick == 70:
                self.currentImage = 1
            elif self.imageTick == 80:
                self.currentImage = 0
                self.imageTick = 0

    def shake(self):
        # move block up and down
        if self.shakingUp:
            self.shakeOffset -= 2
            self.rect.y -= 2
        else:
            self.shakeOffset += 2
            self.rect.y += 2

        # change direction
        if self.shakeOffset == -20:
            self.shakingUp = False

        # stop shaking
        if self.shakeOffset == 0:
            self.shaking = False
            self.shakingUp = True

    def spawn_bonus(self, core):
        # activate block and give bonus
        self.isActivated = True
        self.shaking = True
        self.imageTick = 0
        self.currentImage = 3

        # mushroom bonus
        if self.bonus == 'mushroom':
            core.get_sound().play('mushroom_appear', 0, 0.5)
            if core.get_map().get_player().powerLVL == 0:
                core.get_map().spawn_mushroom(self.rect.x, self.rect.y)

        # coin bonus
        elif self.bonus == 'coin':
            core.get_sound().play('coin', 0, 0.5)
            core.get_map().spawn_debris(self.rect.x + 8, self.rect.y - 32, 1)
            core.get_map().get_player().add_coins(1)
            core.get_map().get_player().add_score(200)

    def destroy(self, core):
        # break block into pieces
        core.get_map().spawn_debris(self.rect.x, self.rect.y, 0)
        core.get_map().remove_object(self)

    def render(self, core):

        # question block
        if self.typeID == 22:
            if not self.isActivated:
                self.update()
            elif self.shaking:
                self.shake()

            core.screen.blit(
                self.image[self.currentImage],
                core.get_map().get_camera().apply(self)
            )

        # brick block (shake when hit)
        elif self.typeID == 23 and self.shaking:
            self.shake()
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))

        # normal render
        else:
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))