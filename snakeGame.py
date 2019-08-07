import pygame , sys, time
import random #for Foor coordinate

check_errors = pygame.init() #it returns errors from pygame (success,errors)
if check_errors[1]>0: 
    print("Had {0} error!! ".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized! ")
    
# Play surface
playSurface =pygame.display.set_mode((720,460))
pygame.display.set_caption('Fatma\'s Snake Game!!! ')


# colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
foodColor = pygame.Color(120,120,120)
blue = pygame.Color(0,0,255)

fpsController = pygame.time.Clock() # frame per second, snake speed


#compSnakePos = [30,10]##
#compSnakeBody = [[30,10],[20,10],[10,10]]

#Coordinates
snakePos = [100, 50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawm = True

direction ='RIGHT'
changeto = direction

score = 0 
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load('crash.wav')


def gameOver():
    myFont =pygame.font.SysFont('monaco',80)
    playSurface.fill(white)

    GOsurf = myFont.render('Game Over!', True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 150)
    playSurface.blit(GOsurf,GOrect)

    displayScore(0)
    
    pygame.display.flip()
    pygame.mixer.music.stop()

    pygame.quit() #pygame exit
    sys.exit() #console exit

def displayScore(choice=1): #default is 1
    sFont =pygame.font.SysFont('monaco',30)
    Ssurf = sFont.render('Score : {0}'.format(score), True,red)
    Srect = Ssurf.get_rect()
    if choice ==1:
        Srect.midtop= (80, 10)
        Ssurf = sFont.render('Score : {0}'.format(score), True,black)
    else:
        Srect.midtop= (360,  120)
    playSurface.blit(Ssurf,Srect)


# Main Loop of Game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT or event.key == ord('d'):
                changeto ='RIGHT'
            if event.key ==pygame.K_LEFT or event.key == ord('a'):
                changeto ='LEFT'
            if event.key ==pygame.K_UP or event.key == ord('w'):
                changeto ='UP'
            if event.key ==pygame.K_DOWN or event.key == ord('s'):
                changeto ='DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.port(pygame.event.Event(QUIT))

    # validation of direction
    if changeto=='RIGHT' and not direction =='LEFT':
        direction ='RIGHT'
    if changeto=='LEFT' and not direction =='RIGHT':
        direction ='LEFT'
    if changeto=='UP' and not direction =='DOWN':
        direction ='UP'
    if changeto=='DOWN' and not direction =='UP':
        direction ='DOWN'

    if direction =='RIGHT':
        snakePos[0] +=10
    if direction =='LEFT':
        snakePos[0] -=10
    if direction =='UP':
        snakePos[1] -=10
    if direction =='DOWN':
        snakePos[1] +=10

    # Snake Body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score +=10
        foodSpawm =False
    else: 
        snakeBody.pop()

    # Food Spawn
    if foodSpawm ==False: 
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawm =True
    
    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green, pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface,foodColor, pygame.Rect(foodPos[0],foodPos[1],10,10))

    if snakePos[0]>710 or snakePos[0]<0:
        pygame.mixer.music.play(-1)
        gameOver()
    if snakePos[1]>450 or snakePos[1]<0:
        pygame.mixer.music.play(-1)
        gameOver()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] ==block[1]:
            screamSound = pygame.mixer.Sound("tail.wav")
            pygame.mixer.music.load('tail.wav')
            pygame.mixer.music.play(-1)
            gameOver()

    displayScore()
    
    pygame.display.flip()
    fpsController.tick(15)

    