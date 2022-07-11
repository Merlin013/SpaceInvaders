import pygame
import random

# initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Add background to the screen
background = pygame.image.load("space_background.png")

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
enemyX_change = 0.8
enemyY_change = 25

# Missile image
missileImg = pygame.image.load("missile.png")
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 1
missile_state = "ready"


# Ready - we can't see the bullet on the screen
# Fire - The bullet is in motion

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))


# Game loop
running = True
while running:
    # RGB - red, green, blue
    screen.fill((75, 150, 100))
    # add background image to persist
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check if its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # can be if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_d:  # can be if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:  # can be if event.key == pygame.K_RIGHT:
                fire_missile(playerX, missileY)

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
        enemyX_change = 0.8
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.8
        enemyY += enemyY_change

    # Missile movement
    if missile_state == "fire":
        fire_missile(playerX, missileY)
        missileY -= missileY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
