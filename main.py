import pygame
from game import Game
pygame.init()

# Fenetre du jeu #
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("WORMS")
screen = pygame.display.set_mode((1920, 1018))
######################

# Charger l'arriere-plan #
background = pygame.image.load('assets/background.png')

# Charger notre jeu #
game = Game()

running = True

#Boucle de jeu #
while running:
    # Applique la fenetre du jeu #
    screen.blit(background, (0, 0))
    #Appliquer l'image de mon joueur #
    screen.blit(game.player.image, game.player.rect)


    # recuperer les projectiles du jeu
    for projectile in game.player.all_projectiles:
        projectile.move()
    # Appliquer l'ensemble des imagse de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #Verifie si le joueur va a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mettre à jour l'écran #
    pygame.display.flip()

    for event in pygame.event.get():
        # Si le joueur ferme la fenetre #
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # Detecte si un joueur presse une touche #
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecte si la touche espace est enclenché pour projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        # Detecte si un joueur ne presse pas une touche #
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

