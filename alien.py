# alien.py
import pygame

class Alien(pygame.sprite.Sprite):
    """класс одного принешльца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """выводи пришельца на экран"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """перемещение пришельцев"""
        self.y += 0.1
        self.rect.y = self.y





