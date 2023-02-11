import pygame

#initialize game
pygame.init()

#screensize
screen = pygame.display.set_mode((800, 800))
screenSize = pygame.display.get_window_size() #returns a tuple (800, 800)


running = True #boolean variable to determine if the game is running or not

#player
def player(playerx, playery):
    playervx = 0
    playervy = 0

    player_image = pygame.image.load("images/whiteRobot.png")
    player_hitbox = player_image.get_rect()

    playerx += playervx
    playery += playervy

    player_hitbox.x = playerx
    player_hitbox.y = playery

    screen.blit(player_image, (playerx, playery))

updatePlayerX = screenSize[0] / 2
updatePlayerY = screenSize[1] / 2

#game loop
while running:
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player(updatePlayerX, updatePlayerY)
    
    if keys[pygame.K_d]: #right
            updatePlayerX += 0.3
    if keys[pygame.K_a]: #left
            updatePlayerX -= 0.3
    if keys[pygame.K_w]: #up
        updatePlayerY -= 0.3
    if keys[pygame.K_s]: #down
        updatePlayerY += 0.3
        
    #creating a border for the whole screen
    if(updatePlayerY >= screenSize[0] - 45):
        updatePlayerY = screenSize[0] - 45
    if(updatePlayerX >= screenSize[0] - 45):
        updatePlayerX = screenSize[0] - 45
    if(updatePlayerY <= 0):
        updatePlayerY = 1
    if(updatePlayerX <= 0):
        updatePlayerX = 1
        
    pygame.display.update()