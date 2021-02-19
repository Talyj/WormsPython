import random
import pygame
import pygame.gfxdraw

from scipy.interpolate import CubicSpline
from sprite import Sprite


BACKGROUND_COLOR = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

class Map(Sprite):
    def __init__(self, game, granularity):
        super().__init__(game)

        self.width = self.game.window.width
        self.height = self.game.window.height
        self.granularity = granularity

        # Create surface
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BACKGROUND_COLOR)

        points = self.get_spline_points()
        self.draw_curve(self.image, points)

        self.rect = self.image.get_rect()
        self.texture_map()




    def draw_line(self, surface, p1, p2):
        pygame.gfxdraw.line(surface, p1[0], p1[1], p2[0], p2[1], WHITE)


    def get_spline_points(self):
        x_values = list(range(0, self.width -1, 100))
        x_values.append(self.width -1)
        y_values = [random.randint(200, self.height -80) for _ in x_values]

        spline = CubicSpline(x_values, y_values)
        x_max = self.width -1
        points = [(x, round(float(spline(x)))) for x in range(0, x_max, self.granularity)]
        points.append((x_max, round(float(spline(x_max)))))
        return points


    def draw_curve(self, surface, points):
        for point_index in range(1, len(points)):
            self.draw_line(surface, points[point_index - 1], points[point_index])


    def texture_map(self):
        texture = pygame.image.load("res/map_texture.png")
        for x in range(self.width):
            for y in range(self.height):
                color = self.image.get_at((x, y))
                if (color == WHITE):
                    for new_y in range(y, self.height):
                        color_texture = texture.get_at((x, new_y))
                        self.image.set_at((x, new_y), color_texture)
                    break
