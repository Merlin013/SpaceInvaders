import pygame
import random
import math
from pygame import mixer


# initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Add background to the screen
background = pygame.image.load("space_background.png")

# Background music
mixer.music.load("One_Against_the_World.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemylist = ["enemy1.png", "enemy2.png", "enemy3.png"]
for j in range(num_of_enemies):
    enemyselected = random.choice(enemylist)
    enemyImg.append(pygame.image.load(enemyselected))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(10, 70))
    enemyX_change.append(0.5 + random.random())
    enemyY_change.append(20)

# Missile image
missileImg = pygame.image.load("missile.png")
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 4
missile_state = "ready"

# explosion image
explosionImg1 = pygame.image.load("explosion.png")
explosionImg2 = pygame.image.load("explode_big.png")
explosionX = 0
explosionY = 0

# Ready - we can't see the bullet on the screen
# Fire - The bullet is in motion

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 25)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 65)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))


def explode(x, y):
    for k in range(70):
        # screen.blit(explosionImg1, (x, y))
        screen.blit(explosionImg2, (x, y))
        pygame.display.update()


def is_collision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(enemyX - missileX, 2)) + math.pow(enemyY - missileY, 2))
    if distance < 30:
        return True
    else:
        return False


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
                if missile_state == "ready":
                    # Get the current X coordinate of the player
                    missile_sound = mixer.Sound("laser.wav")
                    missile_sound.play()
                    missileX = playerX
                    fire_missile(missileX, missileY)

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
    for i in range(num_of_enemies):

        #Game over text
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision detection
        collision = is_collision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            missileY = 480
            missile_state = "ready"
            score_value += 1
            explosionX = enemyX[i]
            explosionY = enemyY[i]
            explode(explosionX, explosionY)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(10, 70)
        enemy(enemyX[i], enemyY[i], i)

    # Missile movement
    if missileY <= 0:
        missileY = 480
        missile_state = "ready"

    if missile_state == "fire":
        fire_missile(missileX, missileY)
        missileY -= missileY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
