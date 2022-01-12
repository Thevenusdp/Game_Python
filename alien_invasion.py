import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """"Загальний клас, що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """"Ініціалізація гри, створення ресурсів гри"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.alients = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """"Розпочинаємо головний цикл гри"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.update()
            self._hide_bullet()
            self._update_sreeen()


    def _check_events(self):
        """"Реакція на натискання клавіатури"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #Клавішу натиснуто
            elif event.type == pygame.KEYDOWN:
                self._cheak_keydonw_events(event)
            elif event.type == pygame.KEYUP:
                self._cheak_keyup_events(event)


    def _cheak_keydonw_events(self, event):
        #Реагування на натиссненя клавіші
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _cheak_keyup_events(self, event):
        #реагування на натискання клавіші
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """"Створити нову кулю"""
        if len(self.bullet) < self.settings.bullet_allowed:  #обмежує кількість куль одночасно на екрані
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _hide_bullet(self):
        """"Видаляємо кулі, що перетнули межу екрану"""
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

    def _create_fleet(self):
        """"Створити флот прибульців"""
        #створити прибульця та визначити їх кількість у ряду
        #відстань між прибульцями дорівнює ширині одного прибульця

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_alien_x = available_space_x // (2*alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height)
                             - ship_height)
        number_rows = available_space_y // (2*alien_height)

        for row_number in range(number_rows):
            #створити перший ряд прибульців
            for alien_number in range(number_alien_x):
                #створити прибульця та поставити його до ряду
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_hight = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height +  2 *  alien.rect.height * row_number
        self.alients.add(alien)



    def _update_sreeen(self):
        # Заново перемалювати екран на кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.alients.draw(self.screen)

        # Показати останній намальований екран
        pygame.display.flip()




if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


