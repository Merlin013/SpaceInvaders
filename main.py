import pygame
import random


# initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

# Player image
playerImg = pygame.image.load("spaceship_icon.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image
enemyImg = pygame.image.load("enemy1.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 125)
enemyX_change = 0.3
enemyY_change = 25

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
running = True
while running:
    # RGB - red, green, blue
    screen.fill((75, 150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check if its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # can be if event.key == pygame.K_LEFT:
                playerX_change = -0.35
            if event.key == pygame.K_d:  # can be if event.key == pygame.K_RIGHT:
                playerX_change = 0.35
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    # The conditions below prevents the player from going out of bounds of the screen.
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # The conditions below are the same as above but for the enemy. - Enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
