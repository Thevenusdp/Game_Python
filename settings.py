class Settings:
    """"Клас для збереження всіх налаштувань"""

    def __init__(self):
        #налаштування екрану
        self.screen_width = 1100
        self.screen_height = 750
        self.bg_color = (20, 20, 100,)
        self.ship_spead = 5.0

        #налаштування кулі
        self.bullet_speed = 2
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullet_allowed = 10

        #налаштування прибульців
        self.alien_speed = 1.0
        self.fleet_drop_speed = 3

        #fleet_direction = 1 означає напрямок руку праворуч; -1 -- ліворуч.
        self.fleet_direction = -1

        #налаштування астероїдів
        self.asteroid_speed = 10

        #налаштування корабля
        self.ship_limit = 3

        #як швидко гра має прискоритись
        self.speed_up_scale = 1.1
        self.intialize_dynamic_setting()

        #як швидко збільшується вартість прибульців
        self.score_scale = 1.5

        #отримання балів
        self.alien_points = 50

    def intialize_dynamic_setting(self):
        self.ship_spead = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #flet_direction 1 представляє напрямок праворуч; -1 -- ліворуч.
        self.fleet_direction = 1

    def icnrease_speed(self):
        """"Збільшення налаштувань швидкості та вартості прибульців"""
        self.ship_spead *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)



