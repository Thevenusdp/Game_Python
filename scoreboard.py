import pygame.font

class Scoreboard:
    """"Клас, що виводить рахунок"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings
        self.stats = ai_game.stats

        #налаштувння шрифту для відображення рахунку
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Підготування зображень з початковим рахунком
        self.prep_score()


    def prep_score(self):
        """"Перетворити рахунок на зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.setting.bg_color)

        #показати рахунок у верхньому правому куті
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """"Показати рахунок на екрані"""
        self.screen.blit(self.score_image, self.score_rect)