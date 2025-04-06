from Game import Game
from Player import Player
import pygame

if __name__ == "__main__":
    game = Game()
    player = Player(x=100, y=500, name="Alba")
    game.set_player(player)
    game.run()

