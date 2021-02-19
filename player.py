import pygame
from projectile import Projectile

## Notre Joueur ##
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player_right.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        #créer une instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_left(self):
        self.image = pygame.image.load('assets/player_left.png')
        self.rect.x -= self.velocity

    def move_right(self):
        self.image = pygame.image.load('assets/player_right.png')
        self.rect.x += self.velocity