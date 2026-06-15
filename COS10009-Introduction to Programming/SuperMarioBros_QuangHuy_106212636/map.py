import pygame as pg
from pytmx.util_pygame import load_pygame

from gameui import GameUI
from bgobject import BGObject
from camera import Camera
from event import Event
from flag import Flag
from const import *
from platform_tile import Platform
from player import Player
from goombas import Goombas
from mushroom import Mushroom
from koopa import Koopa
from tube import Tube
from platformdebris import PlatformDebris
from coindebris import CoinDebris
from text import Text


class Map(object):
 # This class represents the game map, including all its objects, mobs, and logic for updating and rendering them.
 # It loads the map data from a .tmx file, initializes all the game objects, and contains methods for updating the game state and rendering everything on the screen.
    def __init__(self, world_num):
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.text_objects = []
        self.map = 0
        self.flag = None

        self.mapSize = (0, 0)
        self.sky = 0

        self.textures = {}
        self.worldNum = world_num
        self.loadWorld_11()

        self.is_mob_spawned = [False, False]
        self.score_for_killing_mob = 100
        self.score_time = 0

        self.in_event = False
        self.tick = 0
        self.time = 400

        self.oPlayer = Player(x_pos=128, y_pos=351)
        self.oCamera = Camera(self.mapSize[0] * 32, 14)
        self.oEvent = Event()
        self.oGameUI = GameUI()

    def loadWorld_11(self):
        # Load the map data from the .tmx file and initialize all the objects based on the layers and tiles defined in the file.
        tmx_data = load_pygame("worlds/1-1/W11.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))

        # Initialize the map as a 2D list of zeros, which will be filled with Platform and BGObject instances based on the .tmx data.
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        for layer in tmx_data.visible_layers:
            # Loop through every tile in the layer and create the appropriate game objects based on the tile ID and layer name.
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Getting pygame surface
                    image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)

                        if layer.name == 'Foreground':

                              # Special case for "question" blocks: they have 4 frames (1 normal, 3 activated) and I need to load them all so we can switch between them when the player hits the block.
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # activated
                                )

                            # For all other tiles, I just create a Platform object with the image and tile ID. I also add it to the list of objects and to the map grid for collision detection.
                            # The map grid (self.map) is a 2D list where each cell can either be 0 (empty) or contain a Platform or BGObject instance. 
                            # This allows for easy collision detection later on when the player or mobs interact with the environment.
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])

                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1

        # Tubes
        self.spawn_tube(28, 10)
        self.spawn_tube(37, 9)
        self.spawn_tube(46, 8)
        self.spawn_tube(55, 8)
        self.spawn_tube(163, 10)
        self.spawn_tube(179, 10)

        # Mobs
        self.mobs.append(Goombas(736, 352, False))
        self.mobs.append(Goombas(1295, 352, True))
        self.mobs.append(Goombas(1632, 352, False))
        self.mobs.append(Goombas(1672, 352, False))
        self.mobs.append(Goombas(5570, 352, False))
        self.mobs.append(Goombas(5620, 352, False))

        self.map[21][8].bonus = 'mushroom'
        self.map[78][8].bonus = 'mushroom'
        self.map[109][4].bonus = 'mushroom'

        self.flag = Flag(6336, 48)

    def reset(self, reset_all):
        # Reset the map to its initial state. This is called when the player dies or wins, and it clears all mobs, debris, and resets the player and camera to their starting positions. 
        # It also resets the time and score for killing mobs.
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.is_mob_spawned = [False, False]

        self.in_event = False
        self.flag = None
        self.sky = None
        self.map = None

        self.tick = 0
        self.time = 400

        self.mapSize = (0, 0)
        self.textures = {}
        self.loadWorld_11()

        self.get_event().reset()
        self.get_player().reset(reset_all)
        self.get_camera().reset()

    def get_name(self):
        if self.worldNum == '1-1':
            return '1-1'

    def get_player(self):
        return self.oPlayer

    def get_camera(self):
        return self.oCamera

    def get_event(self):
        return self.oEvent

    def get_ui(self):
        return self.oGameUI

    def get_blocks_for_collision(self, x, y):
        # Returns a tuple of blocks around the given (x, y) coordinates to check for collisions. 
        # This is used to determine if the player or mobs are colliding with the environment.
        return (
            self.map[x][y - 1],
            self.map[x][y + 1],
            self.map[x][y],
            self.map[x - 1][y],
            self.map[x + 1][y],
            self.map[x + 2][y],
            self.map[x + 1][y - 1],
            self.map[x + 1][y + 1],
            self.map[x][y + 2],
            self.map[x + 1][y + 2],
            self.map[x - 1][y + 1],
            self.map[x + 2][y + 1],
            self.map[x][y + 3],
            self.map[x + 1][y + 3]
        )

    def get_blocks_below(self, x, y):
        # Returns the blocks directly below the given (x, y) coordinates. 
        # This is used to check if the player or mobs are standing on the ground or a platform.
        return (
            self.map[x][y + 1],
            self.map[x + 1][y + 1]
        )

    def get_mobs(self):
        return self.mobs

    def spawn_tube(self, x_coord, y_coord):
        # Create a Tube object at the given coordinates and add it to the list of tubes.
        self.tubes.append(Tube(x_coord, y_coord))

        # I also add invisible Platform objects in the map grid where the tube is, so that the player and mobs will collide with the tube properly.
        for y in range(y_coord, 12): # 12 because it's ground level.
            for x in range(x_coord, x_coord + 2):
                self.map[x][y] = Platform(x * 32, y * 32, image=None, type_id=0)

    def spawn_mushroom(self, x, y):
        # Create a Mushroom object at the given coordinates and add it to the list of mobs.
        self.get_mobs().append(Mushroom(x, y, True))

    def spawn_goombas(self, x, y, move_direction):
        # Create a Goombas object at the given coordinates and add it to the list of mobs.
        self.get_mobs().append(Goombas(x, y, move_direction))

    def spawn_koopa(self, x, y, move_direction):
        # Create a Koopa object at the given coordinates and add it to the list of mobs.
        self.get_mobs().append(Koopa(x, y, move_direction))

    def spawn_debris(self, x, y, type):
        # Create debris (either platform debris or coin debris) at the given coordinates and add it to the list of debris.
        if type == 0:
            self.debris.append(PlatformDebris(x, y))
        elif type == 1:
            self.debris.append(CoinDebris(x, y))

    def spawn_score_text(self, x, y, score=None):
        # If score is none, it means the player just killed a mob and we want to show the points for killing that mob. 
        #  amount of points for killing a mob will increase: 100, 200, 400, 800...
        if score is None:
            # Show the current score for killing a mob at the given coordinates. 
            # This will be called when the player kills a mob, and it will display the points earned for that kill.
            self.text_objects.append(Text(str(self.score_for_killing_mob), 16, (x, y)))

            # Next score will be bigger
            self.score_time = pg.time.get_ticks()
            if self.score_for_killing_mob < 1600:
                self.score_for_killing_mob *= 2

        # That case for all other situations.
        else:
            self.text_objects.append(Text(str(score), 16, (x, y)))

    def remove_object(self, object):
        # Remove the given object from the game. This is called when a block is destroyed, a mob dies, or a projectile hits something. 
        # It removes the object from the appropriate list and also clears it from the map grid if it's a block.
        self.obj.remove(object)
        self.map[object.rect.x // 32][object.rect.y // 32] = 0

    def remove_text(self, text_object):
        # Remove the given text object from the list of text objects. 
        self.text_objects.remove(text_object)

    def update_player(self, core):
        # Update the player's position, handle input, and check for collisions with the environment and mobs.
        self.get_player().update(core)

    def update_entities(self, core):
        # Update all mobs and check for collisions with the player. 
        for mob in self.mobs:
            mob.update(core)
            if not self.in_event:
                self.entity_collisions(core)

    def update_time(self, core):
        #   Update the remaining time for the level. If the time runs out, the player dies.
        if not self.in_event:
            # The time decreases by 1 every 40 ticks (which is about every 2/3 of a second if the game runs at 60 FPS).
            self.tick += 1
            if self.tick % 40 == 0:
                self.time -= 1
                self.tick = 0
            if self.time == 100 and self.tick == 1:
                core.get_sound().start_fast_music(core)
            elif self.time == 0:
                self.player_death(core)

    def update_score_time(self):
        # Reset the score for killing mobs back to 100 if enough time has passed since the last kill.
        if self.score_for_killing_mob != 100:

            # Delay is 750 ms
            if pg.time.get_ticks() > self.score_time + 750:
                self.score_for_killing_mob //= 2

    def entity_collisions(self, core):
        # Check for collisions between the player and all mobs. 
        # This is called every frame in the update_entities method, and it handles interactions like the player jumping on a Goomba or getting hit by a Koopa shell.
        if not core.get_map().get_player().unkillable:
            for mob in self.mobs:
                mob.check_collision_with_player(core)

    def try_spawn_mobs(self, core):
        # Spawn mobs based on the player's position. 
        # This is used to create the effect of enemies appearing as the player progresses through the level, rather than having all enemies loaded at once.

        if self.get_player().rect.x > 2080 and not self.is_mob_spawned[0]:
            # Spawn a group of Goombas in the middle of the level when the player reaches a certain point.
            self.spawn_goombas(2495, 224, False)
            self.spawn_goombas(2560, 96, False)
            self.is_mob_spawned[0] = True

        elif self.get_player().rect.x > 2460 and not self.is_mob_spawned[1]:
            # Spawn more enemies near the end of the level when the player reaches another point. 
            # This includes Goombas and a Koopa.
            self.spawn_goombas(3200, 352, False)
            self.spawn_goombas(3250, 352, False)
            self.spawn_koopa(3400, 352, False)
            self.spawn_goombas(3700, 352, False)
            self.spawn_goombas(3750, 352, False)
            self.spawn_goombas(4060, 352, False)
            self.spawn_goombas(4110, 352, False)
            self.spawn_goombas(4190, 352, False)
            self.spawn_goombas(4240, 352, False)
            self.is_mob_spawned[1] = True

    def player_death(self, core):
        # Handle the player's death by starting the death event, which will play the death animation and reset the level after a delay.
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_player().numOfLives -= 1

        if self.get_player().numOfLives == 0:
            self.get_event().start_kill(core, game_over=True)
        else:
            self.get_event().start_kill(core, game_over=False)

    def player_win(self, core):
        # Handle the player touching the flag at the end of the level by starting the win event, which will play the flagpole animation and then reset the level after a delay.
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_event().start_win(core)

    def update(self, core):
        # Update the game state every frame. 
        # This includes updating the player, mobs, debris, and handling events like the player dying or winning.

        # All mobs
        self.update_entities(core)

        if not core.get_map().in_event:

            # When player eats a mushroom
            if self.get_player().inLevelUpAnimation:
                self.get_player().change_powerlvl_animation()

            # Unlike the level up animation, player can move there
            elif self.get_player().inLevelDownAnimation:
                self.get_player().change_powerlvl_animation()
                self.update_player(core)

            # Common case
            else:
                self.update_player(core)

        else:
            self.get_event().update(core)

        # Debris from blocks and coins

        for debris in self.debris:
            debris.update(core)

        # Text which represent how mapy points player get
        for text_object in self.text_objects:
            text_object.update(core)

        # Camera stops moving when player dies or touches a flag
        if not self.in_event:
            self.get_camera().update(core.get_map().get_player().rect)

        self.try_spawn_mobs(core)

        self.update_time(core)
        self.update_score_time()

    def render_map(self, core):
        # This function is used to render the main menu background, which is just the map without any mobs or the player.

        core.screen.blit(self.sky, (0, 0))

        for obj_group in (self.obj_bg, self.obj):
            for obj in obj_group:
                obj.render(core)

        for tube in self.tubes:
            tube.render(core)

    def render(self, core):
        # This function is used to render the actual game screen, which includes the map, mobs, debris, and UI.

        core.screen.blit(self.sky, (0, 0))

        for obj in self.obj_bg:
            obj.render(core)

        for mob in self.mobs:
            mob.render(core)

        for obj in self.obj:
            obj.render(core)

        for tube in self.tubes:
            tube.render(core)

        for debris in self.debris:
            debris.render(core)

        self.flag.render(core)

        for text_object in self.text_objects:
            text_object.render_in_game(core)

        self.get_player().render(core)

        self.get_ui().render(core)
