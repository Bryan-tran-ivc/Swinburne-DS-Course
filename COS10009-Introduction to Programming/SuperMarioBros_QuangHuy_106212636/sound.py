import pygame as pg

# Manages loading, playing, and stopping game audio assets
class Sound(object):
    def __init__(self):
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        # Initialize sound dictionary with audio files for music and SFX
        self.sounds['overworld'] = pg.mixer.Sound('sounds/overworld.wav')
        self.sounds['overworld_fast'] = pg.mixer.Sound('sounds/overworld-fast.wav')
        self.sounds['level_end'] = pg.mixer.Sound('sounds/levelend.wav')
        self.sounds['coin'] = pg.mixer.Sound('sounds/coin.wav')
        self.sounds['small_mario_jump'] = pg.mixer.Sound('sounds/jump.wav')
        self.sounds['big_mario_jump'] = pg.mixer.Sound('sounds/jumpbig.wav')
        self.sounds['brick_break'] = pg.mixer.Sound('sounds/blockbreak.wav')
        self.sounds['block_hit'] = pg.mixer.Sound('sounds/blockhit.wav')
        self.sounds['mushroom_appear'] = pg.mixer.Sound('sounds/mushroomappear.wav')
        self.sounds['mushroom_eat'] = pg.mixer.Sound('sounds/mushroomeat.wav')
        self.sounds['death'] = pg.mixer.Sound('sounds/death.wav')
        self.sounds['pipe'] = pg.mixer.Sound('sounds/pipe.wav')
        self.sounds['kill_mob'] = pg.mixer.Sound('sounds/kill_mob.wav')
        self.sounds['game_over'] = pg.mixer.Sound('sounds/gameover.wav')
        self.sounds['scorering'] = pg.mixer.Sound('sounds/scorering.wav')
        self.sounds['shot'] = pg.mixer.Sound('sounds/shot.wav')

    def play(self, name, loops, volume):
        # Play a specific sound with defined loop count and volume level
        self.sounds[name].play(loops=loops)
        self.sounds[name].set_volume(volume)

    def stop(self, name):
        # Immediately halt playback of a specific sound
        self.sounds[name].stop()

    def start_fast_music(self, core):
        # Switch to the accelerated version of the theme for the main level
        if core.get_map().get_name() == '1-1':
            self.stop('overworld')
            self.play('overworld_fast', 99999, 0.5)