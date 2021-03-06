import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"Керування кулями, що випускаються з корабля"""

    def __init__(self, ai_game):
        """"Створення кулі у поточній позиції коробля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #Створення rect кулі у (0, 0) та задати правbльну позицію
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #Зберігати розицію кулі як десяткове значення
        self.y = float(self.rect.y)

    def update(self):
        """"Посунути кулю нагору екраном"""
        #оновити десяткову позицію кулі
        self.y -= self.settings.bullet_speed
        #оновити позицію rect
        self.rect.y = self.y

    def draw_bullet(self):
        """"Намалювати кулю на екрані"""
        pygame.draw.rect(self.screen, self.color, self.rect)