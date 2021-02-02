import pygame


def main():
    running = True
    pygame.init()

    # Create screen

    screen = pygame.display.set_mode((800, 600))
    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
