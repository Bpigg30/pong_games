import pygame, sys, random
pygame.init

#ball movement + player movement
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    #speed isn't one to increase over time
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1.15
def player_animation():
        #keeps bumpers within the borders
    global opponent, player
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
def computer_movement():
    if opponent.top < ball.y:
        opponent.top += player_two_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= player_two_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y = 7 * random.choice((1,-1))
    ball_speed_x = 7 * random.choice((1,-1))

#general setup
pygame.init()
clock = pygame.time.Clock()

# #starting with main window
# screen_width = 1800
# screen_height = 900
# screen = pygame.display.set_mode((screen_width,screen_height))
#pygame.display.set_caption('Pong')

#attempting to make full screen
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')

#game rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#defining the colors in both stated color and RGB value
red = pygame.Color('red')
white = (255,255,255)
black = (0,0,0)
light_grey = ('grey12')

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_one_speed = 0
#player 2 is ai
player_two_speed = 7

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #player one movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_one_speed += 7
            if event.key == pygame.K_UP:
                player_one_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_one_speed -= 7
            if event.key == pygame.K_UP:
                player_one_speed += 7

    ball_animation()
    player_animation()
    computer_movement()



    
    player.y += player_one_speed
    

    #visuals (drawn from top to bottom)
    screen.fill(black)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, red, opponent)
    #for line in middle of screen (anti-alias line)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    pygame.draw.ellipse(screen, white, ball)
    
    #fills the shapes and controls fps
    pygame.display.flip()
    clock.tick(120)