import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/nlo.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """"Повертає істину, якщо прибулець знаходиться на краю екрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """"Змістити положення прибульця праворуч"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

