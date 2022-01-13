import pygame
from pygame.sprite import Sprite


class Asteroid(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/asteroid.png")
        self.rect = self.image.get_rect()
