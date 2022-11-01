# Import and initialize the pygame library
import pygame
from pygame.locals import *
import utili

class Block:
    def __init__(self, loc, x, y, xspd, yspd):
        self.location = loc
        self.x = x 
        self.y = y
        self.x_Speed = xspd
        self.y_Speed = yspd

# initialize pygame
pygame.init()


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
# Set up the drawing window
# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


# set the icon of the window
pygame.display.set_icon(pygame.image.load('./resources/block.jpg'))
# change the title of window
pygame.display.set_caption('Block')


# Things to we are going to use and draw
rect1 = pygame.Rect(250, 100, 300, 100)
bckLoc = pygame.image.load('./resources/block.jpg').convert() # convert_alpha() used for transparent png
block = Block(bckLoc, 300, 300, 3, 5)

# used to draw the rectangles
def drawing():
    block.x += block.x_Speed
    block.y += block.y_Speed
        
    # pygame.draw.rect(surface, color, rectangle)
    pygame.draw.rect(screen, (255, 255, 255), rect1)
    # surface.blit(location, x, y)
    screen.blit(block.location, (block.x, block.y))

# Frame rate of game
FPS = 60
clock = pygame.time.Clock()
blockMovement = 30

# Used for our game loop
running = True

# Game loop
while running:
    # limits the frame rate to what ever FPS is
    clock.tick(FPS)
    
    # checks to see if the user controlled rectangle is hitting the window sodes
    if not utili.find_collision_windowRect(rect1, SCREEN_WIDTH, SCREEN_HEIGHT):
        # get user input
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                
                    if event.key == K_ESCAPE:
                        running = False
                                        
                    if event.key == K_UP:
                        rect1.y-= blockMovement
                
                    if event.key == K_DOWN:
                        rect1.y += blockMovement
                
                    if event.key == K_LEFT:
                        rect1.x -= blockMovement
                    
                    if event.key == K_RIGHT:
                        rect1.x += blockMovement
                    
                elif event.type == pygame.QUIT:
                    running = False
    
    # see if the moving rectangle hits the window
    utili.find_collision_window(block, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # see if the two rectangle hit each other
    utili.find_collision_rect(rect1, block)
        
        
    # Used to fill the background with a color based on RGB
    screen.fill((0,0, 0))
    
    # calls our draw funcution
    drawing()
    
    # update our surfaces
    pygame.display.update()
    


# Tells pygame the program is done
pygame.quit()