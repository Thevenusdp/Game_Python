import sys
import pygame
from settings import Settings
from time import sleep
from ship import Ship
from bullet import Bullet
from alien import Alien
from stars import Stars
from asteroid import Asteroid
from alien_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """"Загальний клас, що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """"Ініціалізація гри, створення ресурсів гри"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.asteroids = Asteroid(self)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self) #табло на екрані
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self._create_fleet()
        self._create_stars()
        self._create_asteroid()
        self.play_button = Button(self, "Play")

    def run_game(self):
        """"Розпочинаємо головний цикл гри"""
        while True:
            self._check_events()
            self._update_asteroids()
            self.ship.blitme()
            self.bullets.update()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            self._update_sreeen()

    def _create_stars(self):
        """"Створює рандомну кількість зірок у рандомних місцях"""
        how_many_stars = 100
        for star in range(how_many_stars):
            star = Stars(self)
            self.stars.add(star)

    def _check_events(self):
        """"Реакція на натискання клавіатури"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                #Клавішу натиснуто
            elif event.type == pygame.KEYDOWN:
                self._cheak_keydonw_events(event)
            elif event.type == pygame.KEYUP:
                self._cheak_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """"Розпочинати гру, коли користувач натисне кнопку `Play`"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #анулювати ігрову статистику
            self.settings.intialize_dynamic_setting()

            #анулювати ігрову статистику
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            #позбавитись надлишку прибульців та куль
            self.aliens.empty()
            self.bullets.empty()

            #створити новий флот та відцентрувати корабель
            self._create_fleet()
            self.ship.center_ship()

            #приховати курсор миші
            pygame.mouse.set_visible(False)

    def _cheak_keydonw_events(self, event):
        #Реагування на натиснненя клавіші
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True

    def _cheak_keyup_events(self, event):
        #реагування на натискання клавіші
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False

    def _fire_bullet(self):
        """"Створити нову кулю"""
        if len(self.bullets) < self.settings.bullet_allowed:  #обмежує кількість куль одночасно на екрані
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """"Видаляємо кулі, що перетнули межу екрану"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _create_asteroid(self):
        """"Створює астероїди у рандомних місцях"""
        how_many_asteroids = 20
        for asteroid in range(how_many_asteroids):
            asteroid = Asteroid(self)
            asteroid.update()
            self.stars.add(asteroid)

    def _update_asteroids(self):
        asteroid = Asteroid(self)
        asteroid.update()


    def _check_asteroid_ship_collision(self):   #### ДОПРАЦЮВАННЯ!!!
        """"Перевіряємо, чи зіштовхнулись корабель та астероїд"""
        collision = pygame.sprite.groupcollide(self.ship, self.asteroids, True, True)
        if self.ship:
            self._ship_hit()

    def _check_bullet_alien_collision(self):
        """"Реакція на зіткненння куль з прибульцямию."""
        #видалити всі кулі та прибульців, що зіткнултся
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)
            self.sb.prep_score()

        if not self.aliens:
            #знищити наявні кулі та поновити флот
            self.bullets.empty()
            self._create_fleet()
            self.settings.icnrease_speed()

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
        alien.rect.y = alien.rect.height + alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """"Оновити позиції всіх прибульців"""
        self._check_fleet_edges()
        self.aliens.update()
        #шукати зіткнення куль із прибульцями
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #шукати. чи котрийсь із прибульців досяг нижнього краю
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """"Перевірити, чи не досяг якийсь прибулець нижнього краю екрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #реагувати так, ніби корабль було підбито
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """"
        Реагує відповідно до того, чи досяг котрийсь із
        прибульців краю екрана
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """"Спуск всього флоту та зміна його напрямку"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """"Реагувати на зіткнення прибульця з кораблем"""
        if self.stats.ship_left > 0:

            #зменшити ship_left
            self.stats.ship_left -= 1

            #позбавитись надлишку прибульців та куль
            self.aliens.empty()
            self.bullets.empty()

            #створити новий флот та відцентрувати корабель
            self._create_fleet()
            self.ship.center_ship()

            #пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_sreeen(self):
        # Заново перемалювати екран на кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        self.stars.draw(self.screen)
        self.asteroids.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_buttom()

        # Показати останній намальований екран
        pygame.display.flip()





if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


