import pygame
from sprite import Sprite
from pygame.transform import scale

class Player(Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("res/player.png")
        self.image = scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 70
        self.gravity = 4

        

    def update(self, event):

        speed = int(200 * self.game.delta/1000)

        if (event.player_left):
            self.rect.x -= speed

        if (event.player_right):
            self.rect.x += speed

        if (event.player_up):
            self.rect.y -= speed

        self.rect.y += self.gravity



