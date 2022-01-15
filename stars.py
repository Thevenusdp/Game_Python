import pygame
from pygame.sprite import Sprite
from random import randint

class Stars(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/Star.png")
        self.rect = self.image.get_rect()
        self.rect.y = randint(1, 750)
        self.rect.x = randint(1, 1100)









