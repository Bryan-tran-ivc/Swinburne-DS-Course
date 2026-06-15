import pygame as pg

from const import *


class Player(object):
    def __init__(self, x_pos, y_pos):
        # Player parameters
        self.numOfLives = 3
        self.score = 0
        self.coins = 0

        self.visible = True
        self.spriteTick = 0
        self.powerLVL = 0

        self.unkillable = False
        self.unkillableTime = 0

        self.inLevelUpAnimation = False
        self.inLevelUpAnimationTime = 0
        self.inLevelDownAnimation = False
        self.inLevelDownAnimationTime = 0

        self.already_jumped = False
        self.next_jump_time = 0
        self.x_vel = 0
        self.y_vel = 0
        self.direction = True
        self.on_ground = False
        
        self.pos_x = x_pos

        self.image = pg.image.load('images/mario/mario.png').convert_alpha()
        self.sprites = []
        self.load_sprites()

        self.rect = pg.Rect(x_pos, y_pos, 32, 32)

    def load_sprites(self):
        # Load all the player sprites for different power levels, animations, and directions.
        self.sprites = [
            # 0 Small, stay
            pg.image.load('images/Mario/mario.png'),

            # 1 Small, move 0
            pg.image.load('images/Mario/mario_move0.png'),

            # 2 Small, move 1
            pg.image.load('images/Mario/mario_move1.png'),

            # 3 Small, move 2
            pg.image.load('images/Mario/mario_move2.png'),

            # 4 Small, jump
            pg.image.load('images/Mario/mario_jump.png'),

            # 5 Small, end 0
            pg.image.load('images/Mario/mario_end.png'),

            # 6 Small, end 1
            pg.image.load('images/Mario/mario_end1.png'),

            # 7 Small, stop
            pg.image.load('images/Mario/mario_st.png'),


            # 8 Big, stay
            pg.image.load('images/Mario/mario1.png'),

            # 9 Big, move 0
            pg.image.load('images/Mario/mario1_move0.png'),

            # 10 Big, move 1
            pg.image.load('images/Mario/mario1_move1.png'),

            # 11 Big, move 2
            pg.image.load('images/Mario/mario1_move2.png'),

            # 12 Big, jump
            pg.image.load('images/Mario/mario1_jump.png'),

            # 13 Big, end 0
            pg.image.load('images/Mario/mario1_end.png'),

            # 14 Big, end 1
            pg.image.load('images/Mario/mario1_end1.png'),

            # 15 Big, stop
            pg.image.load('images/Mario/mario1_st.png'),

        ]

        # Left side
        for i in range(len(self.sprites)):
            self.sprites.append(pg.transform.flip(self.sprites[i], 180, 0))

        # Power level changing, right
        self.sprites.append(pg.image.load('images/Mario/mario_lvlup.png').convert_alpha())

        # Power level changing, left
        self.sprites.append(pg.transform.flip(self.sprites[-1], 180, 0))

        # Death
        self.sprites.append(pg.image.load('images/Mario/mario_death.png').convert_alpha())

    def update(self, core):
        # Update the player's state every frame, including movement, animation, and invincibility time.
        self.player_physics(core)
        self.update_image(core)
        self.update_unkillable_time()

    def player_physics(self, core):
        # Handle player input for movement and jumping, apply gravity, check for collisions with blocks, and handle interactions with the environment like activating blocks or falling off the map.
        if core.keyR:
            self.x_vel += SPEED_INCREASE_RATE
            self.direction = True
        if core.keyL:
            self.x_vel -= SPEED_INCREASE_RATE
            self.direction = False
        if not core.keyU:
            self.already_jumped = False
        elif core.keyU:
            if self.on_ground and not self.already_jumped:
                self.y_vel = -JUMP_POWER
                self.already_jumped = True
                self.next_jump_time = pg.time.get_ticks() + 750
                if self.powerLVL >= 1:
                    core.get_sound().play('big_mario_jump', 0, 0.5)
                else:
                    core.get_sound().play('small_mario_jump', 0, 0.5)

        if not (core.keyR or core.keyL):
            # Decelerate to a stop when no movement keys are pressed, and cap speed at max values.
            if self.x_vel > 0:
                self.x_vel -= SPEED_DECREASE_RATE
            elif self.x_vel < 0:
                self.x_vel += SPEED_DECREASE_RATE
        else:
            if self.x_vel > 0:
                if self.x_vel > MAX_MOVE_SPEED:
                    self.x_vel = MAX_MOVE_SPEED
            if self.x_vel < 0:
                if (-self.x_vel) > MAX_MOVE_SPEED:
                    self.x_vel = -MAX_MOVE_SPEED

        # removing the computational error
        if 0 < self.x_vel < SPEED_DECREASE_RATE:
            self.x_vel = 0
        if 0 > self.x_vel > -SPEED_DECREASE_RATE:
            self.x_vel = 0

        if not self.on_ground:
            # Moving up, button is pressed
            if (self.y_vel < 0 and core.keyU):
                self.y_vel += GRAVITY
                
            # Moving up, button is not pressed - low jump
            elif (self.y_vel < 0 and not core.keyU):
                self.y_vel += GRAVITY * LOW_JUMP_MULTIPLIER
            
            # Moving down
            else:
                self.y_vel += GRAVITY * FALL_MULTIPLIER
            
            if self.y_vel > MAX_FALL_SPEED:
                self.y_vel = MAX_FALL_SPEED

        blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
        # Update horizontal position and handle horizontal collisions
        self.pos_x += self.x_vel
        self.rect.x = self.pos_x
        
        self.update_x_pos(blocks)

        self.rect.y += self.y_vel
        self.update_y_pos(blocks, core)

        # on_ground parameter won't be stable without this piece of code
        coord_y = self.rect.y // 32
        if self.powerLVL > 0:
            coord_y += 1
        for block in core.get_map().get_blocks_below(self.rect.x // 32, coord_y):
            if block != 0 and block.type != 'BGObject':
                if pg.Rect(self.rect.x, self.rect.y + 1, self.rect.w, self.rect.h).colliderect(block.rect):
                    self.on_ground = True

        # Map border check
        if self.rect.y > 448:
            core.get_map().player_death(core)

        # End Flag collision check
        if self.rect.colliderect(core.get_map().flag.pillar_rect):
            core.get_map().player_win(core)

    def set_image(self, image_id):

        # "Dead" sprite
        if image_id == len(self.sprites):
            self.image = self.sprites[-1]
            return

        # Use the proper offset for left-facing sprites.
        # Right-facing sprites are stored first, then the left-facing flipped versions.
        if self.direction:
            sprite_index = image_id + self.powerLVL * 8
        else:
            sprite_index = image_id + 16 + self.powerLVL * 8

        if sprite_index < 0 or sprite_index >= len(self.sprites):
            self.image = self.sprites[-1]
        else:
            self.image = self.sprites[sprite_index]

    def update_image(self, core):
        # Update the player's sprite based on movement and animation state.

        self.spriteTick += 1

        if self.powerLVL in (0, 1):

            if self.x_vel == 0:
                self.set_image(0)
                self.spriteTick = 0

            # Player is running
            elif (
                    ((self.x_vel > 0 and core.keyR and not core.keyL) or
                     (self.x_vel < 0 and core.keyL and not core.keyR)) or
                    (self.x_vel > 0 and not (core.keyL or core.keyR)) or
                    (self.x_vel < 0 and not (core.keyL or core.keyR))
            ):
                             
                if (self.spriteTick > 30):
                    self.spriteTick = 0
                   
                if self.spriteTick <= 10:
                    self.set_image(1)
                elif 11 <= self.spriteTick <= 20:
                    self.set_image(2)
                elif 21 <= self.spriteTick <= 30:
                    self.set_image(3)
                elif self.spriteTick == 31:
                    self.spriteTick = 0
                    self.set_image(1)

            # Player decided to move in the another direction, but hasn't stopped yet
            elif (self.x_vel > 0 and core.keyL and not core.keyR) or (self.x_vel < 0 and core.keyR and not core.keyL):
                self.set_image(7)
                self.spriteTick = 0

            if not self.on_ground:
                self.spriteTick = 0
                self.set_image(4)

    def update_unkillable_time(self):
        # If Mario is currently invincible, count down the time until he becomes vulnerable again.
        if self.unkillable:
            self.unkillableTime -= 1
            if self.unkillableTime == 0:
                self.unkillable = False

    def update_x_pos(self, blocks):
        # Move horizontally and handle collisions with blocks, preventing movement through solid objects.
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                block.debugLight = True
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.x_vel > 0:
                        self.rect.right = block.rect.left
                        self.pos_x = self.rect.left
                        self.x_vel = 0
                    elif self.x_vel < 0:
                        self.rect.left = block.rect.right
                        self.pos_x = self.rect.left
                        self.x_vel = 0

    def update_y_pos(self, blocks, core):
        # Move vertically and handle collisions with blocks, allowing the player to stand on platforms and hit blocks from below.
        self.on_ground = False
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):

                    if self.y_vel > 0:
                        self.on_ground = True
                        self.rect.bottom = block.rect.top
                        self.y_vel = 0

                    elif self.y_vel < 0:
                        self.rect.top = block.rect.bottom
                        self.y_vel = -self.y_vel / 3
                        self.activate_block_action(core, block)

    def activate_block_action(self, core, block):
        # Handle interactions when the player hits a block from below, such as activating question blocks or breaking brick blocks, and awarding points accordingly.
        if block.typeID == 22:
            core.get_sound().play('block_hit', 0, 0.5)
            if not block.isActivated:
                block.spawn_bonus(core)

        # Brick Platform
        elif block.typeID == 23:
            if self.powerLVL == 0:
                block.shaking = True
                core.get_sound().play('block_hit', 0, 0.5)
            else:
                block.destroy(core)
                core.get_sound().play('brick_break', 0, 0.5)
                self.add_score(50)

    def reset(self, reset_all):
        # Reset the player's position and state after dying, and optionally reset all parameters if it's a game over.
        self.direction = True
        self.rect.x = 96
        self.pos_x = 96
        self.rect.y = 351
        if self.powerLVL != 0:
            self.powerLVL = 0
            self.rect.y += 32
            self.rect.h = 32

        if reset_all:
            # If it's a game over, reset all parameters to their initial values.
            self.score = 0
            self.coins = 0
            self.numOfLives = 3

            self.visible = True
            self.spriteTick = 0
            self.powerLVL = 0
            self.inLevelUpAnimation = False
            self.inLevelUpAnimationTime = 0

            self.unkillable = False
            self.unkillableTime = 0

            self.inLevelDownAnimation = False
            self.inLevelDownAnimationTime = 0

            self.already_jumped = False
            self.x_vel = 0
            self.y_vel = 0
            self.on_ground = False

    def reset_jump(self):
        # Reset the player's vertical movement after dying, allowing them to fall down and play the death animation before the level resets.
        self.y_vel = 0
        self.already_jumped = False

    def reset_move(self):
        # Reset the player's horizontal movement after dying, preventing any residual movement from affecting the death animation or level reset.
        self.x_vel = 0
        self.y_vel = 0

    def jump_on_mob(self):
        # This function is called when Mario jumps on a mob, giving him a small bounce effect.
        self.already_jumped = True
        self.y_vel = -4
        self.rect.y -= 6

    def set_powerlvl(self, power_lvl, core):
        # Handle changes to the player's power level, including taking damage, picking up power-ups, and playing the appropriate animations and sounds for each change.
        if self.powerLVL == 0 == power_lvl and not self.unkillable:
            core.get_map().player_death(core)
            self.inLevelUpAnimation = False
            self.inLevelDownAnimation = False

        elif self.powerLVL == 0 and self.powerLVL < power_lvl:
            # If Mario picks up a mushroom, he becomes big. Play the level-up animation and sound, and award points.
            self.powerLVL = 1
            core.get_sound().play('mushroom_eat', 0, 0.5)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=1000)
            self.add_score(1000)
            self.inLevelUpAnimation = True
            self.inLevelUpAnimationTime = 61

        elif self.powerLVL > power_lvl:
            # If Mario takes damage, he becomes smaller and starts the level-down animation.
            core.get_sound().play('pipe', 0, 0.5)
            self.inLevelDownAnimation = True
            self.inLevelDownAnimationTime = 200
            self.unkillable = True
            self.unkillableTime = 200

        else:
            core.get_sound().play('mushroom_eat', 0, 0.5)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=1000)
            self.add_score(1000)

    def change_powerlvl_animation(self):
        # Handle the animation for changing power levels, making Mario flash when taking damage and play the appropriate transformation animations when picking up power-ups.

        if self.inLevelDownAnimation:
            self.inLevelDownAnimationTime -= 1

            if self.inLevelDownAnimationTime == 0:
                self.inLevelDownAnimation = False
                self.visible = True
            elif self.inLevelDownAnimationTime % 20 == 0:
                if self.visible:
                    self.visible = False
                else:
                    self.visible = True
                if self.inLevelDownAnimationTime == 100:
                    self.powerLVL = 0
                    self.rect.y += 32
                    self.rect.h = 32

        elif self.inLevelUpAnimation:
            self.inLevelUpAnimationTime -= 1

            if self.inLevelUpAnimationTime == 0:
                self.inLevelUpAnimation = False
                self.rect.y -= 32
                self.rect.h = 64

            elif self.inLevelUpAnimationTime in (60, 30):
                self.image = self.sprites[-3] if self.direction else self.sprites[-2]
                self.rect.y -= 16
                self.rect.h = 48

            elif self.inLevelUpAnimationTime in (45, 15):
                self.image = self.sprites[0] if self.direction else self.sprites[24]
                self.rect.y += 16
                self.rect.h = 32

    def flag_animation_move(self, core, walk_to_castle):
        # Handle the animation for when Mario touches the flag at the end of the level, including sliding down the pole and walking into the castle, and awarding points based on the remaining time.
        if walk_to_castle:
            self.direction = True

            if not self.on_ground:
                # Slide down the pole
                self.y_vel += GRAVITY if self.y_vel <= MAX_FALL_SPEED else 0

            x = self.rect.x // 32
            y = self.rect.y // 32
            blocks = core.get_map().get_blocks_for_collision(x, y)

            self.rect.x += self.x_vel
            if self.rect.colliderect(core.get_map().map[205][11]):
                # Stop sliding and start walking when reaching the bottom of the pole
                self.visible = False
                core.get_map().get_event().player_in_castle = True
            self.update_x_pos(blocks)

            self.rect.top += self.y_vel
            self.update_y_pos(blocks, core)

            # on_ground works incorrect without this piece of code
            x = self.rect.x // 32
            y = self.rect.y // 32
            if self.powerLVL > 0:
                y += 1
            for block in core.get_map().get_blocks_below(x, y):
                # Check for collision with the ground to stop sliding down the pole
                if block != 0 and block.type != 'BGObject':
                    if pg.Rect(self.rect.x, self.rect.y + 1, self.rect.w, self.rect.h).colliderect(block.rect):
                        self.on_ground = True

        else:
            if core.get_map().flag.flag_rect.y + 20 > self.rect.y + self.rect.h:
                self.rect.y += 3
                # Award points for sliding down the pole based on how far Mario has slid, with more points awarded for sliding further down.

    def add_coins(self, count):
        # Add coins to the player's total when they collect a coin, and update the score accordingly.
        self.coins += count

    def add_score(self, count):
        # Add points to the player's score when they earn points from various actions like defeating enemies, breaking blocks, or collecting power-ups.
        self.score += count

    def render(self, core):
        # Render the player on the screen if they are visible, applying the camera offset to ensure they are drawn in the correct position relative to the game world.
        if self.visible:
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))
