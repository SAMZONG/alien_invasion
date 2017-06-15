# coding = utf-8

import pygame
from pygame.sprite import Sprite

alien_image = '/Users/Alex/Documents/PycharmProjects/alien_invasion/images/alien.png'

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像， 并设置其rect 属性
        self.image = pygame.image.load(alien_image)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
