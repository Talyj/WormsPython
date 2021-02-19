from pygame.sprite import Sprite as PygameSprite

class Sprite(PygameSprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
