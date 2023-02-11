import pygame
from enum import Enum

#set width and height of screen (width, height)
SIZE = (700, 725)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("WordKrunch")
clock = pygame.time.Clock()

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#define directions
class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    NONE = 4
    
#define shapes
class Shape(Enum):
    CIRCLE = 0
    SQUARE = 1
 

class Player(object):
    def __init__(self, x, y, size, direction, color, shape):
        self.x = x
        self.y = y
        self.size = size
        self.direction = Direction.NONE
        self.color = color
        self.shape = shape
        
                
    def getdirection(self):
        #get keys and store new direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = Direction.LEFT
        if keys[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT 
        if keys[pygame.K_UP]:
            self.direction = Direction.UP
        if keys[pygame.K_DOWN]:
            self.direction = Direction.DOWN
    
    def move(self):
        self.getdirection()
        if self.direction == Direction.LEFT:
            self.x -= 10
        if self.direction == Direction.RIGHT:
            self.x += 10
        if self.direction == Direction.UP:
            self.y -= 10
        if self.direction == Direction.DOWN:
            self.y += 10
            
                
    def draw(self):
        if self.shape == Shape.CIRCLE:
            pygame.draw.circle(SCREEN,
                                self.color,
                                (self.x, self.y),
                                self.size)
        else:
            pygame.draw.rect(SCREEN,
                                self.color,
                                pygame.Rect(self.x, self.y, self.size, self.size))

class Enemy(object):
    def __init__(self, x, y, size, direction, color, shape):
        self.x = x
        self.y = y
        self.size = size
        self.direction = Direction.NONE
        self.color = color
        self.shape = shape
        
                
    def draw(self):
        if self.shape == Shape.CIRCLE:
            pygame.draw.circle(SCREEN,
                                self.color,
                                (self.x, self.y),
                                self.size)
        else:
            pygame.draw.rect(SCREEN,
                                self.color,
                                (self.x, self.y, self.size, self.size))

if __name__ == "__main__":
    pygame.init()
    #generate maze
    
    #make player object
    me = Player(10, 10, 10, Direction.NONE, RED, Shape.CIRCLE)
    ghost = Enemy(20, 20, 20, Direction.NONE, GREEN, Shape.SQUARE)
    
    #game loop:
    quit = False
    while not quit:
        clock.tick(60) #limit to 60 frames per second
        
        
        #see if user quit
        for event in pygame.event.get():
                #if user exits game, then quit
                if event.type == pygame.QUIT:
                    quit = True
        
        #move objects   
        me.move()
        
        #redraw window (keep these in order!)
        SCREEN.fill(BLUE)
        me.draw()
        ghost.draw()
        pygame.display.update()
        
    # close window and quit
    pygame.quit()
    
    
#import matt's map code    
#take my screenSize var (line 33)
#import my player method into a spot where it can be used in your running game loop
#put lines 61 and 62 into the a global spot for the game running loop
#put line 66 into your game running while loop
#call player method with updatedPlayerX and Y variables (line 72)
#import my scope statements lines 74-81 into your game running loop
#import lines 83-91 into your game running loop
#this should not cause issues with your code while also allowing mine to live in there well.
