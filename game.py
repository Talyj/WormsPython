from player import Player

## Notre jeu ##
class Game():
    def __init__(self):
        #Genere joueur #
        self.player = Player()
        #Contient les touches actuellement active
        self.pressed = {}

