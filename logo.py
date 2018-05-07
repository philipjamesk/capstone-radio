import pygame


class Logo(object):
    def __init__(self, screen, image, name):
        """Create a logo for each radio station on the display."""
        self.screen = screen

        # Load the image and get make a rect for it
        try:
            self.image = pygame.image.load(image)
        # If the image doesn't load, create a logo from the name
        except Exception:
            self.image = self.make_image(name)

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

    def make_image(self, name):
        """Create an image from the name."""
        pygame.font.init()
        self.name = name
        font = pygame.font.SysFont(None, 72)
        temp_name = name
        text = font.render(temp_name, True, (0, 0, 0))

        width = text.get_width() + 10
        temp_logo = pygame.Surface((width, width))

        pygame.draw.rect(temp_logo, (255, 255, 255), (0, 0, width, width), 0)
        temp_logo.blit(text,
                       (width/2 - text.get_width() // 2,
                        width/2 - text.get_height() // 2))

        pygame.font.quit()
        return temp_logo
