from Game import Game

if __name__ == "__main__":
    game = Game()
    game.start()
    game.update()
    game.display_score_and_lives()
    game.end_game()
    game.update()
    game.remove_opponent()
    game.handle_enemy_conversion()
    game.handle_player_hit()
    game.display_score_and_lives()
    game.end_game()
    game.update()
    game.remove_opponent()
    game.handle_enemy_conversion()
    game.handle_player_hit()
    game.display_score_and_lives()

