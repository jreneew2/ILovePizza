import pygame
from utilities import load_png

class Shelf(pygame.sprite.Sprite):
    def __init__(self, shelfnum):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('shelf.png')

        self.image = pygame.transform.scale(self.image, (100, 500))

        if shelfnum == 0:
            self.x = 180
            self.y = 128
            self.rect.x = 180
            self.rect.y = 128
        elif shelfnum == 1:
            self.x = 460
            self.y = 128
            self.rect.x = 460
            self.rect.y = 128
        elif shelfnum == 2:
            self.x = 740
            self.y = 128
            self.rect.x = 740
            self.rect.y = 128
        else:
            self.x = 1020
            self.y = 128
            self.rect.x = 1020
            self.rect.y = 128
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
