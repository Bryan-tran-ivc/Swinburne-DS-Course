"""
This program demonstrates how to draw various shapes using the Pygame library.
It includes examples of drawing rectangles, polygons, circles, ellipses, lines, and arcs
with different colors and styles.
Please ensure you have Pygame installed in your Python environment to run this code.
Install pygame using `pip install pygame` if you haven't already.

Play around with the parameters of each shape to see how they affect the drawing!
When you are ready create your own Pygame program to draw a picture of your choice using different shapes.

Documentation reference:
https://www.pygame.org/docs/ref/draw.html 
"""
import pygame
from math import pi as PI

# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Shapes")
clock = pygame.time.Clock()

"""
Define colors as constants for better readability.
Colors are defined using RGB values.
"""
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SEA_GREEN = (46, 139, 87)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
WINE_RED = (128, 0, 32)
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)

# Fill the background with white
screen.fill(WHITE)

# Draw a rectangle
"""
draw.rect parameters:
1. Surface to draw on (screen)
2. Color (BLUE) 
3. Rectangle defined as (x, y, width, height)
4. Width of the border (0 for filled)
"""
pygame.draw.rect(screen, BLUE, (150, 100, 200, 100), 0) # Draw filled rectangle

"""
Draw a Polygon (triangle in this case)
draw.polygon parameters:
1. Surface to draw on (screen)
2. Color (RED)
3. List of points defining the polygon [(x1, y1), (x2, y2), (x3, y3), ...]
4. Width of the border (0 for filled)
"""
pygame.draw.polygon(screen, RED, [(400, 300), (500, 100), (600, 300)], 0) # Draw filled triangle
# Set the border to draw an outline
pygame.draw.polygon(screen, RED, [(450, 350), (550, 150), (650, 350)], 5) # Draw triangle outline

# Draw a Circle
""" 
draw.circle parameters:
1. Surface to draw on (screen)
2. Color (GREEN)
3. Center of the circle (x, y)
4. Radius of the circle
5. Width of the border (0 for filled)
"""
pygame.draw.circle(screen, GREEN, (650, 150), 75, 0) # Draw filled circle
# We can also draw a segment of a circle
pygame.draw.circle(screen, GREEN, (100, 100), 50, 0, draw_top_right=True) # Draw circle outline
# Draw an elipse
"""
draw.ellipse parameters:
1. Surface to draw on (screen)
2. Color (BLUE)
3. Rectangle defining the bounding box of the ellipse (x, y, width, height)
4. Width of the border (0 for filled)
"""
pygame.draw.ellipse(screen, BLUE, (100, 400, 200, 100), 0) # Draw filled ellipse

# Draw a line
"""
draw.line parameters:
1. Surface to draw on (screen)
2. Color (WINE_RED)
3. Starting point (x1, y1)
4. Ending point (x2, y2)
5. Width of the line
"""
pygame.draw.line(screen, WINE_RED, (400, 400), (700, 500), 5) # Draw line
pygame.draw.aaline(screen, ORANGE, (400, 500), (700, 400), True) # Draw anti-aliased line

# Draw 4 arcs
"""
draw.arc parameters:
1. Surface to draw on (screen)
2. Color (PURPLE)
3. Rectangle defining the bounding box of the ellipse (x, y, width, height)
4. Start angle in radians
5. End angle in radians
"""
pygame.draw.arc(screen, PURPLE, (50, 250, 100, 100), 0, PI/2, 6) # Quarter arc
pygame.draw.arc(screen, SEA_GREEN, (200, 250, 100, 100), PI/2, PI, 6) # Quarter arc
pygame.draw.arc(screen, MAROON, (350, 250, 100, 100), PI, 3*PI/2, 6) # Quarter arc
pygame.draw.arc(screen, SKY_BLUE, (500, 250, 100, 100), 3*PI/2, 2*PI, 6) # Quarter arc

pygame.display.update() # Call this function to update the display after drawing

# Pygame main loop - For now this just handles quitting the window
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)         # wait until next frame (at 60 FPS)