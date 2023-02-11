import pygame
import math

from board import boards

pygame.init()


WIDTH = 900
HEIGHT = 950
PI = math.pi
player_images = []
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'pacman/assets/player_images/{i}.png'), (35,35)))

player_x = 325
player_y = 245
direction = 0
counter = 0
valid_turns = [False, False, False, False]
direction_command = 0
player_speed = 2

screen_padding = HEIGHT - WIDTH

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf',20)
level = boards
color = 'blue'

def drawboard(level):
    num1 = ((HEIGHT - screen_padding)// 32)
    num2 = (WIDTH // 30)
    for i in range (len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), WIDTH // 225)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), WIDTH // 90)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + num1), WIDTH // 300)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), WIDTH // 300)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1], 0, PI / 2, WIDTH // 300)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, WIDTH // 300)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI, 3 * PI / 2, WIDTH // 300)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2, 2 * PI, WIDTH // 300)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), WIDTH // 300)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), WIDTH // 300)

def draw_player():
    #0-RIGHT 1-LEFT 2-UP 3-DOWN
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))

def check_position(center_x, center_y):
    valid_turns = [False, False, False, False]
    num1 = ((HEIGHT - screen_padding) // 32)
    num2 = (WIDTH // 30)
    num3 = 15
    #check collisions based on center x and y based on +/- num3
    if center_x // 30 < 29:
        if direction == 0:
            if level[center_y // num1][(center_x - num3) // num2] < 3:
                valid_turns[1] = True
        if direction == 1:
            if level[center_y // num1][(center_x + num3) // num2] < 3:
                valid_turns[0] = True
        if direction == 2:
            if level[(center_y + num3) // num1][center_x // num2] < 3:
                valid_turns[3] = True
        if direction == 3:
            if level[(center_y - num3) // num1][center_x // num2] < 3:
                valid_turns[2] = True
    
        if direction == 2 or direction == 3:
            if 12 <= center_x % num2 <= 18:
                if level[(center_y + num3) // num1][center_x // num2] < 3:
                    valid_turns[3] = True
                if level[(center_y - num3) // num1][center_x // num2] < 3:
                    valid_turns[2] = True
            if 12 <= center_y % num1 <= 18:
                if level[(center_y) // num1][(center_x - num2) // num2] < 3:
                    valid_turns[1] = True
                if level[(center_y) // num1][(center_x + num2) // num2] < 3:
                    valid_turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= center_x % num2 <= 18:
                if level[(center_y + num3) // num1][center_x // num2] < 3:
                    valid_turns[3] = True
                if level[(center_y - num3) // num1][center_x // num2] < 3:
                    valid_turns[2] = True
            if 12 <= center_y % num1 <= 18:
                if level[(center_y) // num1][(center_x - num3) // num2] < 3:
                    valid_turns[1] = True
                if level[(center_y) // num1][(center_x + num3) // num2] < 3:
                    valid_turns[0] = True


    else:
        valid_turns[0] = True
        valid_turns[1] = True

    return valid_turns

def move_player(player_x, player_y):
    if direction == 0 and valid_turns[0]:
        player_x += player_speed
    elif direction == 1 and valid_turns[1]:
        player_x -= player_speed
    elif direction == 2 and valid_turns[2]:
        player_y -= player_speed
    elif direction == 3 and valid_turns[3]:
        player_y += player_speed
    return player_x, player_y

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
    else:
        counter = 0    
    
    screen.fill('black')
    drawboard(level)
    draw_player()
    center_x = player_x + 23
    center_y = player_y + 24
    valid_turns = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction
        
    if direction_command == 0 and valid_turns[0]:
        direction = 0
    if direction_command == 1 and valid_turns[1]:
        direction = 1
    if direction_command == 2 and valid_turns[2]:
        direction = 2
    if direction_command == 3 and valid_turns[3]:
        direction = 3

    if player_x > WIDTH:
        player_x = -47
    elif player_x < -50:
        player_x = WIDTH - 3
    


    pygame.display.flip()
pygame.quit()