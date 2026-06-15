import pygame
import sys

# Instructions:  This code also needs to be fixed and finished!
# Both the mouse_x and mouse_y co-ordinate should
# be shown, regardless of whether the mouse has been clicked or not.
# The button should be highlighted when the mouse moves over it
# (i.e it should have a black border around the outside)
# finally, a user has noticed that in this version also sometimes the
# button action occurs when you click outside the button area and vice-versa.


# Global constants
WIN_WIDTH = 640
WIN_HEIGHT = 400


class DemoWindow:

    # set up variables and attributes
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hover Button Test")

        self.clock = pygame.time.Clock()  # Controls frame rate

        self.background = (255, 255, 255)  # WHITE
        self.button_font = pygame.font.SysFont(None, 20)
        self.info_font = pygame.font.SysFont(None, 16)

        self.locs = [60, 60]
        
        # Tracking mouse state
        self.mouse_pos = (0, 0)
        self.is_hovering = False

    # 1. Handle events
    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Using MOUSEMOTION to update hover status only when the mouse moves
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                self.is_hovering = self.mouse_over_button(self.mouse_pos[0], self.mouse_pos[1])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Ensure action only happens if mouse is over the button
                    if self.is_hovering:
                        self.background = (255, 255, 0)  # YELLOW
                    else:
                        self.background = (255, 255, 255)  # WHITE

    # 2. Update game state (e.g., move a character)
    def update(self):
        # Currently nothing updates over time
        pass

    # 3. Draw/Render
    # Draw the background, the button with 'click me' text and text
    # showing the mouse coordinates
    def draw(self):

        # Draw background color
        self.screen.fill(self.background)

        # Draw the rectangle that provides the background.

        # Draw the button
        button_rect = (50, 50, 100, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), button_rect)

        # Highlight the button with a black border if the mouse is over it
        if self.is_hovering:
            pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)

        # Draw the button text
        text_surface = self.button_font.render("Click me", True, (0, 0, 0))
        self.screen.blit(text_surface, (60, 60))

        # Draw the mouse_x position
        info_x = self.info_font.render(f"mouse_x: {self.mouse_pos[0]}", True, (0, 0, 0))
        self.screen.blit(info_x, (0, 350))

        # Draw the mouse_y position
        info_y = self.info_font.render(f"mouse_y: {self.mouse_pos[1]}", True, (0, 0, 0))
        self.screen.blit(info_y, (0, 370))

        # 4. Update the display
        pygame.display.flip()

    
    # This still needs to be fixed!
    def mouse_over_button(self, mouse_x, mouse_y):
        # Correctly checking boundaries: X from 50 to 150, Y from 50 to 100
        if ((mouse_x > 50 and mouse_x < 150) and (mouse_y > 50 and mouse_y < 100)):
            return True
        else:
            return False

    # Pygame Game Loop
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            # 5. Control frame rate
            self.clock.tick(60)  # Limit to 60 FPS


if __name__ == "__main__":
    DemoWindow().run()