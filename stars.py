import random
import pygame
from pygame.sprite import Sprite


class Stars(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/Star.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height








