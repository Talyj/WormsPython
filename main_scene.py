from scene import Scene
from player import Player
from map import Map

import pygame

class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.group = pygame.sprite.Group()

        self.map = Map(game, 5)
        self.group.add(self.map)

        self.player = Player(game)
        self.group.add(self.player)


    def update(self, event):
        self.player.update(event)

    def draw(self):
        self.group.draw(self.game.window.screen)
