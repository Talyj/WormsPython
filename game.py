import pygame
from window import Window
from main_scene import MainScene
from event import Event

class Game:
    def __init__(self):
        self.window_width = 640
        self.window_height = 480
        self.window = Window("WORMS", self.window_width, self.window_height)
        self.event = Event()
        self.main_scene = MainScene(self)

        self.clock = pygame.time.Clock()
        self.delta = 0
        self.end = False # Set this attribute to True ton end the game.


    def update(self):
        self.update_delta()
        self.event.update()

        if self.event.exit:
            self.end = True

        self.main_scene.update(self.event)


    def draw(self):
        self.window.clear()
        self.main_scene.draw()
        self.window.update()

    def update_delta(self):
        self.delta = self.clock.tick(60)
        

    def exit(self):
        pass
