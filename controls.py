import sys
import pygame

def check_events():
    """Respone to controls."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         #Change to next logo
