import pygame as pg
from const import *
from text import Text


class LeaderboardScreen(object):
    def __init__(self, core, runs_tracker):
        self.core = core
        self.runs_tracker = runs_tracker
        
        # Timing
        self.iTime = pg.time.get_ticks()
        self.display_duration = 10000  # 10 seconds
        
        # UI elements
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.bg.fill((0, 0, 0))  # Black background
        
        # Colors (Mario style)
        self.color_gold = (255, 215, 0)
        self.color_white = (255, 255, 255)
        self.color_red = (255, 0, 0)
        self.color_yellow = (255, 255, 0)
        self.color_blue = (33, 33, 222)
        
        # Animation state
        self.animation_tick = 0

    def update(self, core):
        self.animation_tick += 1
        
        # Auto-transition to main menu after duration
        if pg.time.get_ticks() >= self.iTime + self.display_duration:
            core.oMM.currentGameState = 'MainMenu'
            core.get_map().reset(True)
            core.get_mm().runs_tracker.clear_runs()  # Clear runs for new session

    def render(self, core):
        # Draw Mario-style background (blue gradient)
        self._draw_background(core)
        
        # Title with Mario star effect
        title_font = pg.font.Font('fonts/emulogic.ttf', 36)
        title = title_font.render('GAME SESSION RESULTS', True, self.color_gold)
        title_rect = title.get_rect(center=(WINDOW_W // 2, 20))
        core.screen.blit(title, title_rect)
        
        # Draw decorative line
        pg.draw.line(core.screen, self.color_gold, (40, 48), (WINDOW_W - 40, 48), 2)
        
        # Session stats
        stats_font = pg.font.Font('fonts/emulogic.ttf', 18)
        run_count = self.runs_tracker.get_run_count()
        
        stats_text = stats_font.render(f'Total Runs: {run_count}', True, self.color_white)
        stats_rect = stats_text.get_rect(center=(WINDOW_W // 2, 75))
        core.screen.blit(stats_text, stats_rect)
        
        # Get sorted runs
        sorted_runs = self.runs_tracker.get_sorted_runs()
        
        # Title
        lb_title_font = pg.font.Font('fonts/emulogic.ttf', 28)
        lb_title = lb_title_font.render('3 LIVES RANKING', True, self.color_gold)
        lb_title_rect = lb_title.get_rect(center=(WINDOW_W // 2, 110))
        core.screen.blit(lb_title, lb_title_rect)
        
        # Draw life entries in 3 rows
        entry_font = pg.font.Font('fonts/emulogic.ttf', 12)
        small_font = pg.font.Font('fonts/emulogic.ttf', 14)
        tiny_font = pg.font.Font('fonts/emulogic.ttf', 10)
        
        # Define 3 life boxes vertically (more compact)
        start_y = 160
        box_height = 65
        box_margin = 15
        
        if len(sorted_runs) == 0:
            no_runs_text = entry_font.render('No runs completed yet!', True, self.color_white)
            no_runs_rect = no_runs_text.get_rect(center=(WINDOW_W // 2, start_y))
            core.screen.blit(no_runs_text, no_runs_rect)
        else:
            # Show exactly 3 lives (pad with empty if needed)
            display_runs = sorted_runs[:3]
            
            for i in range(3):
                # Draw box for each life
                box_y = start_y + (i * (box_height + box_margin))
                box_rect = pg.Rect(80, box_y, WINDOW_W - 160, box_height)
                
                # Draw border
                border_color = self.color_gold if i < len(display_runs) else (100, 100, 100)
                pg.draw.rect(core.screen, border_color, box_rect, 2)
                
                if i < len(display_runs):
                    run = display_runs[i]
                    
                    # Life number with medal
                    if i == 0:
                        life_display = '★ LIFE 1 (Best) ★'
                        life_color = self.color_gold
                    elif i == 1:
                        life_display = '◆ LIFE 2 ◆'
                        life_color = (192, 192, 192)
                    else:
                        life_display = '● LIFE 3 ●'
                        life_color = (205, 127, 50)
                    
                    life_text = entry_font.render(life_display, True, life_color)
                    life_rect = life_text.get_rect(center=(WINDOW_W // 2, box_y + 8))
                    core.screen.blit(life_text, life_rect)
                    
                    # Score and Time on same line (with small 's' for time)
                    score_str = f'Score: {run["score"]}  |  Time: {run["time"]}'
                    score_text = small_font.render(score_str, True, self.color_yellow)
                    score_rect = score_text.get_rect(center=(WINDOW_W // 2, box_y + 32))
                    core.screen.blit(score_text, score_rect)
                    
                    # Small 's' for seconds (aligned with time number)
                    s_text = tiny_font.render('s', True, self.color_yellow)
                    s_rect = s_text.get_rect(midleft=(score_rect.right - 3, score_rect.centery))
                    core.screen.blit(s_text, s_rect)
                    
                    # Status with color
                    status_color = self.color_gold if run.get('status') == 'WIN' else self.color_red
                    status_str = f"Status: {run.get('status', 'N/A')}"
                    status_text = small_font.render(status_str, True, status_color)
                    status_rect = status_text.get_rect(center=(WINDOW_W // 2, box_y + 50))
                    core.screen.blit(status_text, status_rect)
                else:
                    # Empty life slot
                    empty_text = small_font.render('--- EMPTY ---', True, (100, 100, 100))
                    empty_rect = empty_text.get_rect(center=(WINDOW_W // 2, box_y + 32))
                    core.screen.blit(empty_text, empty_rect)
        
        # Bottom instruction with blinking effect
        instruction_font = pg.font.Font('fonts/emulogic.ttf', 12)
        if (self.animation_tick // 20) % 2 == 0:  # Blinking effect
            instruction = instruction_font.render('PRESS ENTER TO CONTINUE', True, self.color_yellow)
        else:
            instruction = instruction_font.render('PRESS ENTER TO CONTINUE', True, (100, 100, 0))
        instruction_rect = instruction.get_rect(center=(WINDOW_W // 2, WINDOW_H - 25))
        core.screen.blit(instruction, instruction_rect)

    def _draw_background(self, core):
        #Draw Mario Background
        # Draw a gradient effect from dark blue to lighter blue
        for i in range(0, WINDOW_H, 2):
            # Create gradient from blue at top to darker at bottom
            intensity = int(100 + (155 * (i / WINDOW_H)))
            color = (50, 50, intensity)
            pg.draw.line(core.screen, color, (0, i), (WINDOW_W, i), 2)
        
        # Draw decorative clouds (simple)
        self._draw_clouds(core)

    def _draw_clouds(self, core):
       #Draw Mario clouds
        cloud_color = (220, 220, 220)
        # Cloud 1
        pg.draw.circle(core.screen, cloud_color, (80, 40), 8)
        pg.draw.circle(core.screen, cloud_color, (95, 35), 10)
        pg.draw.circle(core.screen, cloud_color, (110, 40), 8)
        
        # Cloud 2
        pg.draw.circle(core.screen, cloud_color, (WINDOW_W - 100, 60), 8)
        pg.draw.circle(core.screen, cloud_color, (WINDOW_W - 85, 55), 10)
        pg.draw.circle(core.screen, cloud_color, (WINDOW_W - 70, 60), 8)

    def handle_input(self, core):
        # User inputs
        if getattr(core, 'keyEnter', False):
            core.oMM.currentGameState = 'MainMenu'
            core.get_map().reset(True)
            core.get_mm().runs_tracker.clear_runs()  # Clear runs for new session

