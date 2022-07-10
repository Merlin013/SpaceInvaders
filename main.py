import pygame

# initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB - red, green, blue
    screen.fill((75, 150, 100))
    pygame.display.update()
