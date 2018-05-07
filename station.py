from logo import Logo


class Station:
    """Creates a single streaming station."""
    def __init__(self, address, image, screen, name):
        self.address = address
        self.logo = Logo(screen, image, name)
        self.is_playing = False
