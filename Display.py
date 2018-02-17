import sys
import pygame

def play():
    #Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    # Make a background
    bg_color = (255, 128, 255)


    #Start the main loop for the radio app
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Add background color to screen
        screen.fill(bg_color)


        # Make the most recently drawn screen visible.
        pygame.display.flip()

play()
