import pygame
import sys
import time
import random

check_error = pygame.init()
if check_error[1] > 0:
    print("found {0} an error".format(check_error))
    sys.exit(-1)
else:
    print("Game Loaded successfully")
#playersurface
playsurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake_Game")
print(playsurface)

#colors
red = (250, 0, 0)
green = (0,250,0)
blue = (0,0,250)
white = (250,250,250)
black = (0,0,0)

#FPS
fpscontroller = pygame.time.Clock()

#important
snakepos = [100,50]
snakebody = [[100,50],[90,50],[80,50]]

foodspan = True
foodpos = [random.randrange(1,80) * 10, random.randrange(1,60) * 10]

direction = "Right"
change_to = direction

score = 0

#display greetings
playsurface.fill(black)
pfont = pygame.font.SysFont("monoco",85)
psurf = pfont.render("SNAKE GAME",True,green)
prect = psurf.get_rect()
prect.midtop = (400,275)
playsurface.blit(psurf,prect)
pygame.display.flip()
time.sleep(3 )

#Game Over
def gameover():
    playsurface.fill(black)
    gfont = pygame.font.SysFont("monoco", 85)
    gsurf = gfont.render("GAME OVER", True, red)
    grect = gsurf.get_rect()
    grect.midtop = (400, 30)
    playsurface.blit(gsurf, grect)
    showscore(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#show score
def showscore( choice = 1):
    sfont = pygame.font.SysFont("monoco", 25)
    sfFont = pygame.font.SysFont("monoco", 45)
    ssurf = sfont.render("Score:{0}".format(score), True, red)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (40,10)
    else:
        ssurf = sfFont.render("Score:{0}".format(score), True, red)
        srect.midtop = (400,200)
    playsurface.blit(ssurf,srect)

#main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.type == ord('d'):
                change_to = "Right"
            if event.key == pygame.K_LEFT or event.type == ord('a'):
                change_to = "Left"
            if event.key == pygame.K_UP or event.type == ord('w'):
                change_to = "Up"
            if event.key == pygame.K_DOWN or event.type == ord('s'):
                change_to = "Down"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

#validating the direction
    if change_to == "Right" and not direction == "Left":
        direction = "Right"
    if change_to == "Left" and not direction == "Right":
        direction = "Left"
    if change_to == "Up" and not direction == "Down":
        direction = "Up"
    if change_to == "Down" and not direction == "Up":
        direction = "Down"

    if direction == "Right":
        snakepos[0] += 10
    if direction == "Left":
        snakepos[0] -= 10
    if direction == "Up":
        snakepos[1] -= 10
    if direction == "Down":
        snakepos[1] += 10

#snake mechanism
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score +=1
        foodspan = False
    else:
        snakebody.pop()
    if foodspan == False:
        foodpos = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]
    foodspan = True

    #drawings
    playsurface.fill(black)
    for pos in snakebody:
        pygame.draw.rect(playsurface,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(playsurface,red, pygame.Rect(foodpos[0], foodpos[1],10,10))
    if snakepos[0] > 800 or snakepos[0] < 0:
        gameover()
    if snakepos[1] > 600 or snakepos[1] < 0:
        gameover()

    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameover()

    showscore()
    pygame.display.flip()
    fpscontroller.tick(20)






























