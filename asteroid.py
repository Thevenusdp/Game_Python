import pygame
from pygame.sprite import Sprite
from random import randint

class Asteroid(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.y = randint(1, 1000)
        self.rect.x = randint(1, 1000)



    def update(self):
        self.rect.y += self.settings.asteroid_speed


