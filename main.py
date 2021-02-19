#!/usr/bin/python3

from game import Game

if __name__ == "__main__":
    game = Game()
    while not game.end:
        game.update()
        game.draw()
    game.exit()
