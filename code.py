import pygame
import time
import random

#initializing game
pygame.init()

#Game setting
snake_speed =10
window_x=720
window_y=450

#defining color(R,G,B)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)

#window
pygame.display.set_caption('SnakeGame')
game_window=pygame.display.set_mode((window_x,window_y))

#FPS controller
fps=pygame.time.Clock() #fps controls how fast the game runs

#snake initial position and body
snake_position=[100,50]
snake_body=[
    [100,50], #head
    [90,50], #bodyko first part
    [80,50], #body second part
    [70,50] #tail 
    ]
#fruit position
fruit_position=[random.randrange(1,(window_x//10))*10,random.randrange(1,(window_y//10))*10]
#window_x//10 -> its dividing the window size by 10 pixel ->720/10=72
#random.randrange(1,72) gives ramdom number from 1 to 72
#then *10 turns it back to normal actual pixel 
fruit_spawn=True #fruit appears

#default snake direction for when the game starts
direction="RIGHT"
change_to=direction 

#initial score
score=0
#score funtion
def show_score(choice,color,font,size): 
    score_font=pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score : ' + str(score), True, green)
    #makes the text appear like this "Score : 0" ,applies color and renders it
    score_rect = score_surface.get_rect()
    # keeps score_surface in rectangular box
    if choice==1:
        score_rect.topleft=(10,10)
    elif choice==2:
        score_rect.midtop=(window_x/2,15)
    game_window.blit(score_surface, score_rect)
    #for displaying score in game window

#displaying game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4) #displays in middle top
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip() #flip-> updates screen
    time.sleep(3) #displays for 3sec
    pygame.quit()
    quit()

#main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # pygame clean
            quit()         # exits program
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to='UP'
            elif event.key==pygame.K_DOWN:
                change_to='DOWN'
            elif event.key==pygame.K_LEFT:
                change_to='LEFT'
            elif event.key==pygame.K_RIGHT:
                change_to='RIGHT'
    #to avoid 2 directions at same time
    if change_to=='UP' and direction !='DOWN':
        direction='UP'
    if change_to=='DOWN' and direction !='UP':
        direction='DOWN'
    if change_to=='RIGHT' and direction !='LEFT':
        direction='RIGHT'
    if change_to=='LEFT' and direction !='RIGHT':
        direction='LEFT' 
    
    #Moving the snake [x,y]=[0,1]
    if direction=='UP':
        snake_position[1]-=10 #if direction is up ,y coordinate is decreased by 10
    if direction=='DOWN':
        snake_position[1]+=10 # if down y coordinate increased by 10 
    if direction=='LEFT':
        snake_position[0]-=10 #x is decreased by 10
    if direction=='RIGHT':
        snake_position[0]+=10
    
    #how snake body is increased
    snake_body.insert(0,list(snake_position))
    if snake_position[0]==fruit_position[0] and snake_position[1]==fruit_position[1]:
        score+=10
        fruit_spawn=False #fruit disappears
    else:
        snake_body.pop()
    
    if not fruit_spawn: #checks if fruit has been eaten and if yes creates a new one
        while True:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
            if fruit_position not in snake_body:
                break
        fruit_spawn=True
    game_window.fill(black) #creates a new frame with updated snake and fruit

    for pos in snake_body: #loople iterates in every block of snake
        pygame.draw.rect(game_window,blue,pygame.Rect(pos[0],pos[1],10,10))
       #pygame.rect(x,y,width,height) for snake body and draws the body in green colour in form of rectangl
    pygame.draw.rect(game_window,white,pygame.Rect(fruit_position[0],fruit_position[1],10,10))
    #this is for fruit

    #game over 
    if snake_position[0] < 0 or snake_position[0] >window_x -10 :
        game_over() #if snake goes too left or right
    if snake_position[1] < 0 or snake_position[1]>window_y -10:
        game_over()#up and down
    
    #if snake collides with itself
    for block in snake_body[1:]:
        if snake_position[0]==block[0] and snake_position[1]==block[1]:
            game_over()
    
    show_score(1,white,'Times New Roman',20)
    pygame.display.update()
    fps.tick(snake_speed)

