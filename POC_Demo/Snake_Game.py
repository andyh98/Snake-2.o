#importing necessary libraries
import pygame, sys

#a function made to execute other files from the system
def runfile(runfilename):
  with open(runfilename,"r") as rnf:
    exec(rnf.read())

pygame.init()

#while loop required to always refresh the page
while True:
    game = pygame.display.set_mode((800, 610))
    game.fill([213, 219, 219])
    mousepos = pygame.mouse.get_pos() #checking mouse position
    mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
    pygame.display.set_caption("Lets Play")
    title_font = pygame.font.SysFont("monospace", 80)

    #Adding the title
    gamename = title_font.render('SNAKE GAME', True, (255, 0, 0))
    game.blit(gamename,(150,80))
    
    #Adding the play game button
    if (270 <= mousepos[0] <= 270+250 and 505 <= mousepos[1] <= 555 ):
      #checks if the mouse is hovering over the button
        pygame.draw.rect(game,[100,100,100], [270,505,250,50], 0)
        #checking if the button is clicked
        if mouseclick[0] == 1:
            runfile('Snake_2.o_Demo.py')
            
    else:
        pygame.draw.rect(game,[180,180,180], [270,505,250,50], 0)

    playgame_font = pygame.font.SysFont("comicsansms", 40)
    gamebutton = playgame_font.render('GAME TIME', True, (0, 0, 200))
    game.blit(gamebutton,(275,500))

    #Taking user name
    UserName = playgame_font.render('NAME:', True, (0, 250, 0))
    game.blit(UserName,(50,200))

    #Asking user for theme
    ThemeOption = playgame_font.render('THEMES:', True, (0, 200, 0))
    game.blit(ThemeOption,(50,300))

    #Asking user for speed 
    SpeedOption = playgame_font.render('SPEED:', True, (0, 150, 0))
    game.blit(SpeedOption,(50,400))

    #If user wants to quit
    pygame.draw.rect(game,[180,180,180], [650,550,130,55], 0)
    Quit = playgame_font.render('QUIT', True, (0, 0, 0))
    game.blit(Quit,(650,550))
    if ( 650 <= mousepos[0] <= 650+130 and 550 <= mousepos[1] <= 550 +55):
      #checks if the mouse is hovering over the button
        #checking if the button is clicked
        if mouseclick[0] == 1:
          #print ("quiting")
          #pygame.display.quit()
          pygame.quit()
          sys.exit()
    
    pygame.display.update()




