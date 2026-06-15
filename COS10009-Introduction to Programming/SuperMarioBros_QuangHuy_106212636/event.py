import pygame as pg

from const import *


class Event(object):
    # This class manages cutscenes like dying or winning the level
    def __init__(self):

        # 0 = Death animation, 1 = Winning animation
        self.type = 0

        self.delay = 0
        self.time = 0
        self.x_vel = 0
        self.y_vel = 0
        self.game_over = False
        self.death_recorded = False

        self.player_in_castle = False
        self.tick = 0
        self.score_tick = 0
        self.win_time = 0  # Stores time left when Mario enters the castle

    def reset(self):
        # Reset all variables when starting a new level
        self.type = 0
        self.delay = 0
        self.time = 0
        self.x_vel = 0
        self.y_vel = 0
        self.game_over = False
        self.death_recorded = False
        self.player_in_castle = False
        self.tick = 0
        self.score_tick = 0
        self.win_time = 0

    def start_kill(self, core, game_over):
        # Start the death animation where Mario pops up and falls off screen
        self.type = 0
        self.delay = 4000
        self.y_vel = -4
        self.time = pg.time.get_ticks()
        self.game_over = game_over

        # Stop level music and play the death sound
        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('death', 0, 0.5)

        # Change Mario's sprite to the "dead" image
        core.get_map().get_player().set_image(len(core.get_map().get_player().sprites))

    def start_win(self, core):
        # Trigger the animation for touching the flagpole
        self.type = 1
        self.delay = 2000
        self.time = 0

        # Switch music to the level clear theme
        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('level_end', 0, 0.5)

        # Set Mario to his climbing pose and position him on the pole
        core.get_map().get_player().set_image(5)
        core.get_map().get_player().x_vel = 1
        core.get_map().get_player().rect.x += 10

        # Award bonus score based on how much time is left
        if core.get_map().time >= 300:
            core.get_map().get_player().add_score(5000)
            core.get_map().spawn_score_text(core.get_map().get_player().rect.x + 16, core.get_map().get_player().rect.y, score=5000)
        elif 200 <= core.get_map().time < 300:
            core.get_map().get_player().add_score(2000)
            core.get_map().spawn_score_text(core.get_map().get_player().rect.x + 16, core.get_map().get_player().rect.y, score=2000)
        else:
            core.get_map().get_player().add_score(1000)
            core.get_map().spawn_score_text(core.get_map().get_player().rect.x + 16, core.get_map().get_player().rect.y, score=1000)

    def update(self, core):

        # Logic for when Mario dies
        if self.type == 0:
            # Apply gravity to the dead sprite
            self.y_vel += GRAVITY * FALL_MULTIPLIER if self.y_vel < 6 else 0
            core.get_map().get_player().rect.y += self.y_vel

            # After the delay, decide whether to restart or show leaderboard
            if pg.time.get_ticks() > self.time + self.delay:
                if not self.death_recorded:
                    # Save the score and time to the leaderboard before resetting
                    player = core.get_map().get_player()
                    final_score = player.score
                    final_time = core.get_map().time
                    core.get_mm().runs_tracker.add_run(final_score, final_time, status='LOSE')
                    self.death_recorded = True
                
                if not self.game_over:
                    # Restart the level
                    core.get_map().get_player().reset_move()
                    core.get_map().get_player().reset_jump()
                    core.get_map().reset(False)
                    core.get_sound().play('overworld', 9999999, 0.5)
                else:
                    # Show high scores
                    core.get_mm().show_leaderboard(core)

        # Logic for when Mario wins
        elif self.type == 1:

            if not self.player_in_castle:
                # Slide down the pole if not at the bottom yet
                if not core.get_map().flag.flag_omitted:
                    core.get_map().get_player().set_image(5)
                    core.get_map().flag.move_flag_down()
                    core.get_map().get_player().flag_animation_move(core, False)

                else:
                    # Walk automatically into the castle
                    self.tick += 1
                    if self.tick == 1:
                        core.get_map().get_player().direction = False
                        core.get_map().get_player().set_image(6)
                        core.get_map().get_player().rect.x += 20
                    elif self.tick >= 30:
                        core.get_map().get_player().flag_animation_move(core, True)
                        core.get_map().get_player().update_image(core)

            else:
                # Mario is inside the castle, now count down the remaining time for extra points
                if core.get_map().time > 0:
                    if self.win_time == 0:
                        self.win_time = core.get_map().time
                    
                    self.score_tick += 1
                    if self.score_tick % 10 == 0:
                        core.get_sound().play('scorering', 0, 0.5)

                    core.get_map().time -= 1
                    core.get_map().get_player().add_score(50)

                else:
                    # Once time hits zero, save the win to the leaderboard
                    if self.time == 0:
                        self.time = pg.time.get_ticks()
                        final_score = core.get_map().get_player().score
                        core.get_mm().runs_tracker.add_run(final_score, self.win_time, status='WIN')

                    elif pg.time.get_ticks() >= self.time + self.delay:
                        # Final screen
                        core.get_mm().show_leaderboard(core)