import pygame
from pygame.constants import K_q

class Event:
    def __init__(self):
        self.exit = False
        self.player_left = False
        self.player_right = False
        self.player_up = False
        self.player_down = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

            if event.type == pygame.KEYDOWN:
                key = event.key

                if key == pygame.K_q:
                    self.player_left = True

                if key == pygame.K_d:
                    self.player_right = True

                if key == pygame.K_z:
                    self.player_up = True

                if key == pygame.K_s:
                    self.player_down = True 


            if event.type == pygame.KEYUP:
                key = event.key

                if key == pygame.K_q:
                    self.player_left = False

                if key == pygame.K_d:
                    self.player_right = False

                if key == pygame.K_z:
                    self.player_up = False

                if key == pygame.K_s:
                    self.player_down = False 