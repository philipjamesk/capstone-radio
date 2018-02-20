import sys
import pygame

def check_events(station):
    """Respone to controls."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                return 'right'
            if event.key == pygame.K_LEFT:
                return 'left'
