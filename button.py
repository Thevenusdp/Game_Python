import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #задати розміри та властивості кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #створити об'єкт rect кнопки та відцентрувати  його
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self. screen_rect.center

        #повідомлення на кнопці показати один раз
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """"Перетворити текст на зображення та помістити поцентру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_buttom(self):
        """"Намалювати кнопку порожню, а потім -- повідомлення"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
