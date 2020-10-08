import pygame
import sys
import random

pygame.init()
window = pygame.display.set_mode((480,480))
green = [153, 255, 153]
blue = [0, 204, 204]
red = [204, 0, 0]
black = [0, 0, 0]
pygame.display.set_caption("Snake Game")
game_over = False
pygame.font.init()

x = 150
y = 220

x_change = 0
y_change = 0
score_counter = 0
dtime = pygame.time.Clock()

font = pygame.font.SysFont('courier new', 20, bold = True)
snake_length = 1
snake_list = []

applex = round(random.randrange(0, 450) / 10.0) * 10.0
appley = round(random.randrange(0, 450) / 10.0) * 10.0

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, blue, [x[0], x[1], 25, 25])

def reset():
    global x 
    global y 
    global score_counter
    global x_change
    global y_change
    global snake_length
    global snake_list
    x = 150
    y = 220
    score_counter = 0
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1

def eat():
    global score_counter
    global applex
    global appley
    global snake_length
    score_counter += 1
    applex = round(random.randrange(0, 450) / 10.0) * 10.0
    appley = round(random.randrange(0, 450) / 10.0) * 10.0
    snake_length += 1
    #print("Hit!")
    
def game():
    global game_over
    global x
    global y
    global x_change
    global y_change
    global snake_length
    global snake_list
    #snake_length = 1
    #snake_list = []
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0
 
        if x >= 480 or x < 0 or y >= 480 or y < 0:
            reset()

        x += x_change
        y += y_change
        window.fill(green)
        pygame.draw.rect(window, red, [applex, appley, 20, 20])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]
 
        for j in snake_list[:-1]:
            if j == snake_Head:
                reset()
 
        snake(snake_list)
        #pygame.draw.rect(window,blue,[x,y,25,25])
        text = font.render('Score:' + str(score_counter), True, black)
        window.blit(text, (10,5))
        pygame.display.update()

        if applex <= x <= applex + 20 and appley <= y <= appley + 20:
            eat()
            
        if applex <= x + 25 <= applex + 20 and appley <= y + 25 <= appley + 20:
            eat()
  


        dtime.tick(10)
    
    pygame.quit()
    quit()

game()