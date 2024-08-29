#standard set up
import pygame
from random import randint
pygame.init()

#setting width and height of window

screen_x = 500
screen_y = 500
win = pygame.display.set_mode((screen_x,screen_y))

pygame.display.set_caption("My Game")

white = (255,255,255)
black = (0,0,0)

x = randint(40,400)
y = randint(40,400)
width = 20
height = 20
vel = 10

speed = 40
# 0 - (- direction) , 1 - (+ direction)
direction = 0
# 0 - x-axis , 1 - y-axis
axis = 0

run = True

while run:
    pygame.time.delay(speed) #create a delay to prevent any unwanted behaviour

    #events are anything that happens from the user
    #we loop through the list of events that happen by the user's actions
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        #Each event type has an integer assigned to it. KEYDOWN has the code 2
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                    axis = 0;direction=-1
            if (event.key == pygame.K_RIGHT):
                    axis = 0;direction=1
            if (event.key == pygame.K_UP):
                    axis = 1;direction=-1
            if (event.key == pygame.K_DOWN):
                    axis = 1;direction=1

    #Snake moving depending on axis and direction
    if (axis):
        y += vel*direction
    else:
        x += vel*direction


    if x < 0:
        #x = 0
        x = screen_x - height

    if y < 0:
        #y = 0
        y = screen_y - width

    if y > screen_y - width:
        #y = 500 - width
        y = 0
    if x > screen_x - height:
        #x = 500 - height
        x = 0

    win.fill(white)
    #all colors are defined in RGB with Pygame
    pygame.draw.rect(win,(255,0,0), (x,y,width, height))
    #we have to update the display to see the drawing of our object. Since it does
    #not automatically update
    pygame.display.update()

#Quit the game
pygame.quit()
