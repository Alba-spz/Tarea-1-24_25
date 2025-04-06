from Player import Player
from Boss import Boss
from Opponent import Opponent
import pygame
class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.lives = 3
        self.opponent = Opponent(x=300, y=100, color=(255, 255, 0))
        self.is_running = False

    def set_player(self, player):
        self.player = player
        print(f"Player {self.player.name} has been set.")

    def start(self):
        self.is_running = True
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Lógica para actualizar el estado del juego
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        if self.player and self.player.lives > 0 and not self.opponent:
            print("Victory! You defeated the final boss and won the game!")
        else:
            print("Game ended! Better luck next time.")

    def convert_enemy_to_star(self):
        if self.is_running:
            self.score += 1
            print(f"Enemy converted to star! Current score: {self.score}")
        else:
            print("Cannot convert enemy to star. The game is not running.")

    def display_score_and_lives(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10)) 
        lives_text = font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 50))

    def remove_opponent(self):
        if self.opponent:
            print(f"Opponent {self.opponent.name} defeated!")
            self.opponent = None
            # Logic to spawn the final boss
            self.spawn_final_boss()

    def handle_enemy_conversion(self):
        if self.is_running and self.player:
            self.convert_enemy_to_star(self)
            if not self.opponent:  # If no opponent, spawn the final boss
                self.spawn_final_boss()

    def handle_player_hit(self):
        if self.player and self.is_running:
            self.player.lives -= 1
            print(f"Player hit! Lives left: {self.player.lives}")
            if self.player.lives <= 0:
                print("Player has no lives left. Game over!")
                self.end_game()

    def spawn_final_boss(self):
        if self.is_running:
            boss_image = pygame.image.load("boss.png")
            self.opponent = Boss(x=300, y=100, image=boss_image, lives=5, speed=2 * self.player.speed)
            print("The final boss has appeared! It moves twice as fast!")

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Juego de disparos")
        clock = pygame.time.Clock()

        self.is_running = True
        while self.is_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move('left')
            if keys[pygame.K_RIGHT]:
                self.player.move('right')
            if keys[pygame.K_UP]:
                self.player.move('up')
            if keys[pygame.K_DOWN]:
                self.player.move('down')
            if keys[pygame.K_SPACE]:
                self.player.shoot() 

            self.opponent.move('left')  # Move the opponent

            for shot in self.player.shots:
                shot.move()

            screen.fill((0, 0, 0))
            self.player.draw(screen)
            self.opponent.draw(screen)
            self.display_score_and_lives(screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    
       