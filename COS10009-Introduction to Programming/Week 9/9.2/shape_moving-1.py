import pygame
import sys

# Constants

WIDTH = 400
HEIGHT = 500
SHAPE_DIM = 50

# Instructions:
# Fix the following code so that:
# 1. The shape also can be moved up and down
# 2. The shape does not move out of the window area

# Global Variables
shape_x = WIDTH // 2
shape_y = HEIGHT // 2

# Initialization
def init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shape Moving")
    return screen

# Update Logic
def update():
    global shape_x, shape_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if shape_x < (WIDTH - SHAPE_DIM):
            shape_x += 3

    if keys[pygame.K_LEFT]:
        if shape_x > 0:
            shape_x -= 3

    if keys[pygame.K_DOWN]:
        if shape_y < (HEIGHT - SHAPE_DIM):
            shape_y += 3

    if keys[pygame.K_UP]:
        if shape_y > 0:
            shape_y -= 3


# Draw
def draw(screen):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (shape_x, shape_y, SHAPE_DIM, SHAPE_DIM))
    pygame.display.flip()


# Main Loop
def main():
    screen = init()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update()
        draw(screen)
        clock.tick(60)


if __name__ == "__main__":
    main()