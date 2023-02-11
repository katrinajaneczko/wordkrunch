import pygame

#game idea

'''
Goal of the game: to boost confidence in pronounciation and reading skills while having fun
    Experience: winning in games and challenging myself has always helped boost my confidence in some aspect
        I wanted to take this 
Start of game: pronounciation check
During game:
    We spawn player
    We spawn enemies
    We play "pacman"
    every some number of pellets we do a pronounciation check
    every time you beat a prounounciation check we spawn a big pellet
    you need 2 big pellets to win
    once you have 2 big pellets
    pause the game
    spawn text on screen telling the player to "remember the word that shows" and to "move to the corresponding exit"
    we flash a word on screen (give a count down to get ready) (this will be the correct word) "animal"
    then we flash a word over exit 1 (could be a decoy or the right word)
    then flash a word over exit 2
    then flash a word over exit 3
    then resume game and let player win or lose
'''


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

    #creating "player"
    player_image = pygame.image.load("images/whiteRobot.png") #player image
    player_hitbox = player_image.get_rect()

    #player velocity (if to be implemented later)
    playerx += playervx
    playery += playervy

    #scale the player
    scaled_player = pygame.transform.scale(player_image, (35, 35))

    #give the hitboxes updates
    player_hitbox.x = playerx
    player_hitbox.y = playery

    screen.blit(scaled_player, (playerx, playery)) #initializing our new player image and position

#adaptable player location
updatePlayerX = screenSize[0] / 2
updatePlayerY = screenSize[1] / 2

#game loop
while running:
    keys = pygame.key.get_pressed() #this is the on key click listener
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player(updatePlayerX, updatePlayerY)
    
    if keys[pygame.K_d]: #right
            updatePlayerX += 0.15
    if keys[pygame.K_a]: #left
            updatePlayerX -= 0.15
    if keys[pygame.K_w]: #up
        updatePlayerY -= 0.15
    if keys[pygame.K_s]: #down
        updatePlayerY += 0.15
        
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