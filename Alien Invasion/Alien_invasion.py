import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load("background.png")

#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# title & captions
pygame.display.set_caption("Alien shooter")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
running = True

# player
playerimg = pygame.image.load("spaceship1.png")
playerx = 370
playery = 480
playerx_change = 0

#multiple enemies
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
# ENEMY
no_of_enemy = 6
for i in range(no_of_enemy):
    enemyimg.append(pygame.image.load("ufo.png"))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(2)
    enemyy_change.append(40)

# BULLET
bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bullet_change = 10
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
testx = 10
testy = 10

#Game over
over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score(x, y):
    score = font.render("score " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    down_text = over_font.render("score "+ str(score_value), True, (0, 255, 0))
    screen.blit(over_text, (200, 250))
    screen.blit(down_text, (250, 300))

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
while running:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # seeing which key is presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    # spaceship check boundaries
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # enemy movements
    for i in range(no_of_enemy):
        if enemyy[i] > 440:
            for j in range(no_of_enemy):
                enemyy[i] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 2
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -2
            enemyy[i] += enemyy_change[i]
        # collision
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            attack_sound = mixer.Sound("explosion.wav")
            attack_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value += 1

            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i], i)
    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullet_change

    player(playerx, playery)
    show_score(testx,testy)
    pygame.display.update()
