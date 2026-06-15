import pygame
#Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Shapes")
clock = pygame.time.Clock()

#Define colors
WHITE = (255, 255, 255)
BLUE = (135,206,250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SEA_GREEN = (46, 139, 87)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
WINE_RED = (128, 0, 32)
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)
GRAY = (150, 150, 150)

# Fill the background with white
screen.fill(BLUE)

# ===== Green Circle  =====
pygame.draw.circle(screen, GREEN, (400, 620), 250)

# ===== Rectangle =====
pygame.draw.rect(screen, GRAY, (330, 320, 140, 200))

# ===== Triangle =====
pygame.draw.polygon(screen, RED, [
    (300, 320),   # left
    (500, 320),   # right
    (400, 240)    # top
])

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    clock.tick(60)   