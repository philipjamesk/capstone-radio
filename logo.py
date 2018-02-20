import pygame

class Logo(object):
    def __init__(self, screen, image):
        """Create a logo for each radio station on the display."""
        self.screen = screen

        # Load the image and get make a rect for it
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put logo at center of screen_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the logo at current location."""
        self.screen.blit(self.image, self.rect)
