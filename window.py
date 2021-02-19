import pygame

class Window:
    def __init__(self, title, width, height):
        # Set the window shape and background color.
        background_color = (255,255,255)
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(background_color)

        # Set the window title.
        pygame.display.set_caption(title)

    def clear(self):
        pygame.display.flip()

    def update(self):
        pygame.display.update()
