# importing pygame for the game, time for frame rate and random for food positions
import pygame
import time
import random

# initializing pygame modules
pygame.init()

# defining colours using RGB - CHANGEABLE
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# defining dimensions of game window - CHANGEABLE
dis_width = 800
dis_height = 600

# creating game window with caption
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - ACE')

# to control frame rate
clock = pygame.time.Clock()

# defining size of snake block and speed of snake - CHANGEABLE
snake_block = 10
snake_speed = 15

# defining font style - CHANGEABLE
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# drawing snake on game window
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# to display any message on the game window
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():

    # setting game_over and game_close variables to false (game still on)
    game_over = False
    game_close = False

    # initializing starting position of snake game (at center of screen)
    x1 = dis_width / 2
    y1 = dis_height / 2

    # to track change of position of snake (0 at the start)
    x1_change = 0
    y1_change = 0

    # to store coordinates of snake's body
    snake_List = []

    # to store length of snake's body
    Length_of_snake = 1

    # defining initial random position of food in game window
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # as long as game_over is false (game is on)
    while not game_over:

        # if the player has lost
        while game_close == True:

            # setting background color to blue
            dis.fill(blue)

            # displaying using message function
            message("You Lost! Press Q-Quit or P-Play Again", red)

            # updating game window to reflect messsage
            pygame.display.update()

            # for every event since last iteration
            for event in pygame.event.get():

                # if a key has been pressed
                if event.type == pygame.KEYDOWN:

                    # if 'q' has been pressed (quit)
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    # if 'p' has been pressed (play again)
                    if event.key == pygame.K_p:
                        gameLoop()

        # for every event since last iteration
        for event in pygame.event.get():

            # if use closes game window
            if event.type == pygame.QUIT:
                game_over = True

            # if a key has been pressed
            if event.type == pygame.KEYDOWN:

                # if it is the left arrow -> snake x changes 
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0

                # if it is the right arrow -> snake x changes 
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    
                # if it is the up arrow -> snake y changes 
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    
                # if it is the down arrow -> snake y changes 
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # if snake has collided with game window boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # changing snake's position according to movement    
        x1 += x1_change
        y1 += y1_change

        # colouring background
        dis.fill(blue)

        # drawing food onto game window
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # position of snake's head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        # if snake is longer than required
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # if snake has collided with own body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # draws snake on game window
        our_snake(snake_block, snake_List)

        # updating game window to reflect snake drawing
        pygame.display.update()

        # if snake comes in contact with food
        if x1 == foodx and y1 == foody:

            # changing position of food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            # increasing length of snake
            Length_of_snake += 1

        # limits frame rate
        clock.tick(snake_speed)

    # stopping pygame modules
    pygame.quit()

    # ending program
    quit()

# calling gameLoop function
gameLoop()

