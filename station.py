from logo import Logo

class Station:
    """Creates a single streaming station."""
    def __init__(self, address, image, screen):
        self.address = address
        self.logo = Logo(screen, image)
        self.is_playing = False
