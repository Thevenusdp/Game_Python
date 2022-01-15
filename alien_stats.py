class GameStats:
    """"Відстежуваання статистики гри"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.ship_left = 3
        # розпочати гру в активному стані
        self.game_active = False


    def reset_stats(self):
        """"Ініціалізація статистики, що може змінюватись впродовж гри"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
