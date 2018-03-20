import pygame

class Logo(object):
    def __init__(self, screen, image):
        """Create a logo for each radio station on the display."""
        self.screen = screen

        # Load the image and get make a rect for it
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Put logo at y center and off screen
        self.rect.centerx = -40
        self.rect.centery = self.screen_rect.centery

    def changex(self, x):
        """Change the centerx of logo to a by value of x."""
        self.rect.centerx = self.rect.centerx + x

    def setx(self, x):
        """Set the centerx of logo to a new value of x."""
        self.rect.centerx = x

    def station_is_playing(self):
        """Test if logo of station is in the center of the screen."""
        if self.centerx >= 120 and self.centerx <= 200:
            return True
        else:
            return False

    def blitme(self):
        """Draw the logo at current location."""
        self.screen.blit(self.image, self.rect)
