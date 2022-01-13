class Settings:
    """"Клас для збереження всіх налаштувань"""

    def __init__(self):
        #налаштування екрану
        self.screen_width = 1100
        self.screen_height = 750
        self.bg_color = (20, 20, 100,)
        self.ship_spead = 3

        #налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullet_allowed = 5


