# Import and initialize the pygame library
import pygame

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


# Used for our game loop
running = True

# Game loop
while running:

    # Used to make sure the window doesn't close until user closes the program
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Used to fill the background with a color based on RGB
    screen.fill((255,0, 100))
    
    # RGB
    color = (255, 255, 255)
    
    # makes a rectangle
    # Rect(left, top, width, height)
    pygame.draw.rect(screen, color, pygame.Rect(200, 190, 100, 100))
    
    # Use one of these two fucntions
    
    # Flip the display
    # will update the contents of the entire display
    #pygame.display.flip()
    
    # updates the back ground 
    # allows to update a portion of the screen, instead of the entire area of the screen. 
    # Passing no arguments, updates the entire display
    # update(rectangle_list)
    pygame.display.update()


# Tells pygame the program is done
pygame.quit()