import pygame

class Ship:
    """"Керування кораблем"""

    def __init__(self, ai_game):
        """"Інціалізація корабля та його початкової позиції"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load("images/space_ship2.png")
        self.rect = self.image.get_rect()

        #Створювати кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom

        #Зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)

        #Індикатор руху
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """"Оновлюємо поточну позицію корабля на основі індикатора руху"""

        #оновити значення ship.x а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_spead
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_spead


        #оновити об'єкт rect з self.x
        self.rect.x = self.x





    def blitme(self):
        """"Намалювати корабль у його поточному місці"""
        self.screen.blit(self.image, self.rect)