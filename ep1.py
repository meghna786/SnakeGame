import pygame
import random
import os

pygame.mixer.init()

pygame.init()

green=(46,204,113)
yellow=(243,156,18)
red=(234,32,39)
purple=(217,128,250)
maroon=(131,52,113)
blue=(27,20,100)

#display screen
sWidth=800
sHeight=500
gameDisplay=pygame.display.set_mode((sWidth,sHeight))
pygame.display.set_caption("Snakes")
pygame.display.update()
font=pygame.font.SysFont(None,40)

backImage=pygame.image.load("snake.gif")
backImage=pygame.transform.scale(backImage,(sWidth,sHeight)).convert_alpha()


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameDisplay.blit(screen_text,[x,y])

def drawingSnake(gameDisplay,color, snakeList ,snake_size1,snake_size2):
    for x,y in snakeList:
        pygame.draw.rect(gameDisplay,color,[x,y, snake_size1, snake_size2])

clock=pygame.time.Clock()

def welcomeScreen():
    exitGame=False
    while not exitGame:
        gameDisplay.fill(maroon)
        gameDisplay.blit(backImage,(0,0))
        text_screen("Welcome to Snakes",blue,220,200)
        text_screen("Press Space Bar to play",blue,200,250)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exitGame=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("vision.mp3")
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(60)


#game loop
def gameLoop() :
    # variables
    exitGame = False
    gameOver = False
    pos_x = 45
    pos_y = 55
    snake_size1 = 20
    snake_size2 = 20
    framePerSecond = 60
    vel_x = 0
    vel_y = 0
    food_x = random.randint(20, sWidth / 2)
    food_y = random.randint(20, sHeight / 2)
    food_size = 20
    score = 0
    init_velocity = 5
    snakeList = []
    snakeLength = 1

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w"):
            f.write("0")

    with open("highscore.txt", "r") as f:
        highScore = f.read()

    while not exitGame:
        if gameOver:
            with open("highscore.txt", "w") as f:
                f.write(str(highScore))

            gameDisplay.fill(purple)
            text_screen("Game Over!Press Enter to continue",maroon,sWidth/6,sHeight/2)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitGame=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcomeScreen()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitGame=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x=init_velocity
                        vel_y=0
                    if event.key == pygame.K_LEFT:
                        vel_x=-init_velocity
                        vel_y=0
                    if event.key == pygame.K_UP:
                        vel_y=-init_velocity
                        vel_x=0
                    if event.key == pygame.K_DOWN:
                        vel_y=init_velocity
                        vel_x=0

                    if event.key==pygame.K_u:
                        score+=10

            pos_x=pos_x+vel_x
            pos_y=pos_y+vel_y


            if abs(pos_x-food_x)<11 and abs(pos_y-food_y)<11:
                score+=10
                food_x = random.randint(20, sWidth / 2)
                food_y = random.randint(20, sHeight / 2)
                snakeLength +=5
                if score>int(highScore):
                    highScore=score


            gameDisplay.fill(green)
            text_screen("Score :" + str(score) +"    High Score :" +str(highScore),blue, 5, 5)
            pygame.draw.rect(gameDisplay,red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(pos_x)
            head.append(pos_y)
            snakeList.append(head)

            if len(snakeList)>snakeLength:
                del snakeList[0]

            if head in snakeList[:-1]:
                gameOver=True
                pygame.mixer.music.load("gameOver.mp3")
                pygame.mixer.music.play()


            if pos_x<0 or pos_x>sWidth or pos_y<0 or pos_y>sHeight :
                gameOver= True
                pygame.mixer.music.load("gameOver.mp3")
                pygame.mixer.music.play()

            #pygame.draw.rect(gameDisplay,yellow,[pos_x,pos_y,snake_size1,snake_size2])
            drawingSnake(gameDisplay,yellow,snakeList,snake_size1,snake_size2)
        pygame.display.update()
        clock.tick(framePerSecond)


    pygame.quit()
    quit()
welcomeScreen()
gameLoop()