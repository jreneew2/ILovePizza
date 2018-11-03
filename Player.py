import pygame
from utilities import load_png

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #pygame.display.init()
        self.image, self.rect = load_png('kang.png')
        #self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-64, -64)

        self.isMoving = False
        self.key = pygame.K_m #can't create an empty variable or something smh
        
        self.x = 0
        self.y = 415
        self.rect.x = 0
        self.rect.y = 415

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def reinit(self):
        self.x = 0
        self.y = 415
        self.rect.x = 0
        self.rect.y = 415

    def move(self, passKey):
        self.isMoving = True
        self.key = passKey

    def draw(self, screen):
        if self.isMoving:
            if self.key == pygame.K_UP and self.rect.y > 10:
                self.rect.y -= 10
            elif self.key == pygame.K_DOWN and self.rect.y < 500:
                self.rect.y += 10
            elif self.key == pygame.K_RIGHT and self.rect.x < 1000:
                self.rect.x += 10
            elif self.key == pygame.K_LEFT and self.rect.x > 10:
                self.rect.x -= 10
                
        screen.blit(self.image, (self.rect.x, self.rect.y))
