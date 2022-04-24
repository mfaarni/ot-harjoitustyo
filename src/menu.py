import pygame 
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import sys 
from game import run_game
from time import sleep
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (SCREEN_WIDTH,SCREEN_HEIGHT) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  

quit_button_width = SCREEN_WIDTH-100
quit_button_height = SCREEN_HEIGHT+100

start_button_width = SCREEN_WIDTH-100
start_button_height = SCREEN_HEIGHT-200
  
# defining a font 
quit_font = pygame.font.SysFont('Corbel',50) 
start_font = pygame.font.SysFont('Corbel',100) 
  
# rendering a text written in 
# this font 
text_quit = quit_font.render('QUIT' , True , color) 
text_start=start_font.render('START', True, color)
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if quit_button_width/2 <= mouse[0] <= quit_button_width/2+140 and quit_button_height/2 <= mouse[1] <= quit_button_height/2+40: 
                pygame.quit() 
                sys.exit()
                  
            if start_button_width/2-80 <= mouse[0] <= start_button_width/2+220 and start_button_height/2-20 <= mouse[1] <= start_button_height/2+80:
                for i in range(18):
                    screen.fill((180-i*10,180-i*10,180-i*10))
                    pygame.display.update()
                    sleep(0.01)
                run_game()
    # fills the screen with a color 
    screen.fill((180,230,180)) 
    
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if quit_button_width/2 <= mouse[0] <= quit_button_width/2+140 and quit_button_height/2 <= mouse[1] <= quit_button_height/2+40: 
        pygame.draw.rect(screen,color_light,[quit_button_width/2,quit_button_height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[quit_button_width/2,quit_button_height/2,140,40]) 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if start_button_width/2-80 <= mouse[0] <= start_button_width/2+220 and start_button_height/2-20 <= mouse[1] <= start_button_height/2+80: 
        pygame.draw.rect(screen,color_light,[start_button_width/2-80,start_button_height/2-25,300,100]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[start_button_width/2-80,start_button_height/2-25,300,100]) 
      
    # superimposing the text onto our button 
    screen.blit(text_quit , (quit_button_width/2+25,quit_button_height/2+5)) 
    screen.blit(text_start , (start_button_width/2-40,start_button_height/2-10)) 
      
    # updates the frames of the game 
    pygame.display.update() 